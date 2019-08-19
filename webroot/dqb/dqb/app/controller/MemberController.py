from django.views.decorators.csrf import csrf_exempt
from app.model.MemberModel import QyMember,MemberLister,MemberSerializer,Member_feedback
from app.model.PayModel import QyPay,PaySerializer
from app.model.AdminModel import QyAuditing,AuditingSerializer
from base.my_page import mypage
from base.myjson import JSONResponse
from base.Var import appid,appsecret
from django.db import transaction
import requests
import json
import time
import os



@csrf_exempt
def UserGetOpenID(request):
    '''
    根据前端code码返回相应的openID
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            js_code = data.get('code')
            requestString = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(
                APPID=appid, SECRET=appsecret, JSCODE=js_code)
            r = requests.get(requestString).json()
            return JSONResponse(0,r)
        except Exception as e:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def MemberRegistration(request):
    '''
    用户登录时拉取用户信息
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            data = request.GET
            # 判断用户是否已注册
            with transaction.atomic():
                if QyMember.objects.filter(openid=data.get('openid')):
                    user = QyMember.objects.get(openid=data.get('openid'))
                    if user.avatar.startswith('http'):
                        user.avatar = data.get('avatar', user.avatar)
                    user.nickname = data.get('nickname', user.nickname)
                    user.save()
                else:
                    user = QyMember(openid=data.get('openid'),
                                    avatar=data.get('avatar'),
                                    nickname=data.get('nickname'),
                                    add_time=int(time.time())
                                    )
                    user.save()
                serializer = Member_feedback(user, many=False)
                return JSONResponse(0, serializer.data)
        except Exception as e:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)



@csrf_exempt
def get_member_info(request):
    '''
    获取当前用户信息
    '''
    if request.method == 'GET':
        try:
            user_info = QyMember.objects.get(openid=request.GET.get('openid'))
            # 返回JSON字符串
            serializer = MemberLister(user_info, many=False)
            return JSONResponse(0,serializer.data)
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def change_member_info(request):
    '''
    根据请求信息对当前用户信息进行更改
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            open_id = data.get('openid')
            # 获取登录用户
            user = QyMember.objects.get(openid=open_id)
            with transaction.atomic():
                try:
                    if data.get('avatar') and (not user.avatar.startswith('http')):
                        os.remove(user.avatar)
                except:
                    pass
                if data.get('avatar'):
                    user.avatar = data.get('avatar', user.avatar)
                user.age = data.get('age', user.age)
                user.profession = data.get('profession', user.profession)
                user.phonenum = data.get('phonenum', user.phonenum)
                user.save()
            # 返回JSON字符串
            serializer = Member_feedback(user, many=False)
            return JSONResponse(0,serializer.data)
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def select_member_list(request):
    '''
    根据条件获取指定用户列表
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            phone_num = json.loads(request.body).get('phoneNum')
            nick_name = json.loads(request.body).get('nickName')
            page = json.loads(request.body).get('page')
            if nick_name:
                user_list = QyMember.objects.filter(nickname__contains=nick_name)
            elif phone_num:
                user_list = []
                # 查询手机号不为空的用户
                for x in QyMember.objects.filter(phonenum__isnull=False):
                    if str(x.phonenum).__contains__(str(phone_num)):
                        user_list.append(x)
            else:
                user_list = QyMember.objects.all()
            pag = mypage(page, user_list)
            serializer = MemberSerializer(pag['page_list'], many=True)
            return JSONResponse(0, serializer.data, pag['page_sum'], pag['page_count'])
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def Transaction_details(request):
    '''
    获取当前用户所有交易明细
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            openid = request.GET.get('openid')
            member_id = QyMember.objects.get(openid=openid).id
            pay = QyPay.objects.filter(member_id=member_id).order_by('-id')
            pag = mypage(request.GET.get('page'), pay)
            serializer = PaySerializer(pag['page_list'], many=True)
            return JSONResponse(0, serializer.data, pag['page_sum'], pag['page_count'])
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)


@csrf_exempt
def Boolean(request):
    '''
    返回审核状态
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            info = QyAuditing.objects.get(pk=1)
            # 返回JSON字符串
            serializer = AuditingSerializer(info, many=False)
            return JSONResponse(0, serializer.data)
        except:
            return JSONResponse(1000)
    else:
        return JSONResponse(1054)

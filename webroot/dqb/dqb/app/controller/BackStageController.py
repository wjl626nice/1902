from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth import authenticate, login,logout
from app.model.FeedbackModel import QyFeedback,Feedback
from app.model.MemberModel import QyMember
from app.model.AdminModel import Admin_user
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from base.myjson import JSONResponse
from base.my_page import mypage
import json
import time


@csrf_exempt
def createAdmin(request):
    '''
    用户注册
    :param request: 用户名,邮箱,密码
    :return: 成功/失败
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with transaction.atomic():
                username = data.get('username')
                email = data.get('email')
                password = data.get('password')
                if User.objects.filter(username=username):
                    return JSONResponse(1077)
                user = User.objects.create_user(username, email, password)
                user.save()
                return JSONResponse(3004)
        except:
            return JSONResponse(3003)


@csrf_exempt
def setAdminPassword(request):
    '''
    修改密码
    :param request: username
    :return: 成功/失败
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with transaction.atomic():
                username = data.get('username')
                old_password = data.get('old_password')
                new_password = data.get('new_password')
                if old_password == new_password:
                    return JSONResponse(3010)
                user = User.objects.get(username=username)
                ret = user.check_password(old_password)
                if ret:
                    user.set_password(new_password)
                    user.save()
                    return JSONResponse(0,{'username':username})
                else:
                    return JSONResponse(3005)
        except Exception as e:
            return JSONResponse(3009)




@csrf_exempt
def resetPassword(request):
    '''
    重置密码
    :param request: username
    :return: 成功/失败
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with transaction.atomic():
                username = data.get('username')
                user = User.objects.get(username=username)
                user.set_password('123456')
                user.save()
                return JSONResponse(0, {'username': username})
        except Exception as e:
            return JSONResponse(3009)


@csrf_exempt
def log_in(request):
    '''
    登录
    :param request: username,password
    :return:
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    with transaction.atomic():
                        login(request, user)
                        return JSONResponse(0,{'username':user.username})
                else:
                    return JSONResponse(2001)
            else:
                return JSONResponse(3005)
        except Exception as e:
            return JSONResponse(1006)


@csrf_exempt
def log_out(request):
    '''
    登出
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            with transaction.atomic():
                logout(request)
                return JSONResponse(0)
        except:
            return JSONResponse(1001)



def adminAll(request):
    '''
    获取所有后台用户
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            username = request.GET.get('username')
            if username:
                objs = User.objects.filter(username__icontains=username)
                if not objs:
                    return JSONResponse(2000)
            else:
                objs = User.objects.all()
            page = mypage(request.GET.get('page'), objs)
            s = Admin_user(page['page_list'],many=True)
            return JSONResponse(0,s.data,page['page_sum'],page['page_count'])
        except:
            return JSONResponse(1054)



@csrf_exempt
def delete_admin(request):
    '''
    删除后台用户
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            with transaction.atomic():
                data = json.loads(request.body)
                id = data.get('admin_id')
                cursor = connection.cursor()
                cursor.execute('delete from auth_user where id='+str(id))
                return JSONResponse(0)
        except Exception as e:
            return JSONResponse(1056)




@csrf_exempt
def createFeedback(request):
    '''
    反馈意见
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            openid = data.get('openid')
            content = data.get('content')
            member_id = QyMember.objects.get(openid=openid).id
            with transaction.atomic():
                obj = QyFeedback(
                    member_id=member_id,
                    content=content,
                    add_time=str(time.time())
                )
                obj.save()
                return JSONResponse(0)
        except:
            return JSONResponse(9999)




def getFeedbackAll(request):
    '''
    按条件查询所有的反馈意见
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            phone = request.GET.get('phone')
            nickname = request.GET.get('nickname')
            state = request.GET.get('state')

            if nickname or phone:
                member_id = []
                if phone and nickname:
                    member = QyMember.objects.filter(phonenum=phone,nickname=nickname)
                    for x in member:
                        member_id.append(x.id)
                elif phone and (not nickname):
                    member = QyMember.objects.filter(phonenum__icontains=phone)
                    for y in member:
                        member_id.append(y.id)
                elif nickname and (not phone):
                    member = QyMember.objects.filter(nickname__icontains=nickname)
                    for z in member:
                        member_id.append(z.id)
                # print(member_id)
                objs = QyFeedback.objects.filter(member_id__in=member_id).order_by('-add_time')
            elif state:
                objs = QyFeedback.objects.filter(Feedback_state=int(state)).order_by('-add_time')
            else:
                objs = QyFeedback.objects.all().order_by('-add_time')

            pag = mypage(request.GET.get('page'), objs)
            serializer = Feedback(pag['page_list'], many=True)
            return JSONResponse(0,serializer.data,pag['page_sum'],pag['page_count'])
        except Exception as e:
            return JSONResponse(1054)


@csrf_exempt
def upFeedbackState(request):
    '''
    修改反馈状态(是否已查看)
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with transaction.atomic():
                obj = QyFeedback.objects.get(pk=int(data['Feedback_id']))
                obj.Feedback_state = int(data.get('state',obj.Feedback_state))
                obj.save()
                return JSONResponse(0,{'id':obj.id,'state':obj.Feedback_state})
        except:
            return JSONResponse(1057)
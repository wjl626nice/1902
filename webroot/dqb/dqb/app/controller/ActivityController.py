from app.model.ActivityModel import QyActivity,Act_info
from django.views.decorators.csrf import csrf_exempt
from app.model.MemberModel import QyMember
from base.myjson import JSONResponse
from django.db import transaction
from base.mybase64 import MyFile
from base.my_page import mypage
import json
import time
import os



@csrf_exempt
def Activity_info(request):
    '''
    获取指定活动详情
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            obj = QyActivity.objects.get(pk=request.GET.get('pk'))
            serializer = Act_info(obj, many=False)
            return JSONResponse(0,serializer.data)
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)



@csrf_exempt
def Activity_org_list(request):
    '''
    获取我曾经组织过的活动列表
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            originator_id = QyMember.objects.get(
                openid=request.GET.get('openid')).id
            obj = QyActivity.objects.filter(
                originator_id=originator_id,
                activity_state=2
            ).order_by('-id')
            # 进行分页
            pag = mypage(request.GET.get('page'), obj)
            serializer = Act_info(pag['page_list'], many=True)
            return JSONResponse(0,serializer.data,pag['page_sum'])
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)


@csrf_exempt
def Activity_org_sum(request):
    '''
    获取我曾经组织过的活动数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            originator_id = QyMember.objects.get(
                openid=request.GET.get('openid')).id
            obj = len(QyActivity.objects.filter(
                originator_id=originator_id,activity_state=2))
            return JSONResponse(0,{'sum':obj})
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)


@csrf_exempt
def Activity_create(request):
    '''
    创建活动
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            with transaction.atomic():
                originator_id = QyMember.objects.get(
                    openid=data.get('openid')).id
                obj = QyActivity(
                    notice=data.get('notice'),
                    activity_time=data.get('activity_time'),
                    address_province=data.get('address_province'),
                    address_city=data.get('address_city'),
                    address_area=data.get('address_area'),
                    address_detailed=data.get('address_detailed'),
                    formater=data.get('formater', 0),
                    type=data.get('type', 0),
                    upper_limit=data.get('upper_limit'),
                    lower_limit=data.get('lower_limit'),
                    is_limit=data.get('is_limit', 0),
                    limit_time=data.get('limit_time'),
                    price="%.2f" % data.get('price',0.00),
                    activity_img=data.get('activity_img'),
                    originator_id=originator_id,
                    add_time=str(int(time.time())),
                    is_irres=data.get('is_irres',0),
                    irres_time = data.get('irres_time')
                )
                obj.save()
                serializer = Act_info(obj, many=False)
                return JSONResponse(0,serializer.data)
        except Exception as a:
            return JSONResponse(1007)
    else:
        return JSONResponse(1055)



@csrf_exempt
def Activity_up(request):
    '''
    修改指定活动
    :param request:
    :return:
    '''
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            obj = QyActivity.objects.get(
                pk=data.get('pk'),activity_state=1)
        except:
            return JSONResponse(1007)
        try:
            with transaction.atomic():
                try:
                    activity_img = data.get('activity_img')
                    # 修改活动图片并且有历史图片时，删除旧图片
                    if eval(obj.activity_img) and activity_img:
                            for a in eval(obj.activity_img):
                                os.remove("./{}".format(a))
                except:
                    pass
                obj.activity_img = data.get('activity_img',obj.activity_img)
                obj.notice = data.get('notice', obj.notice)
                obj.activity_time = data.get('activity_time', obj.activity_time)
                obj.address_province = data.get('address_province', obj.address_province)
                obj.address_city = data.get('address_city', obj.address_city)
                obj.address_area = data.get('address_area', obj.address_area)
                obj.address_detailed = data.get('address_detailed', obj.address_detailed)
                obj.formater = data.get('formater', obj.formater)
                obj.type = data.get('type', obj.type)
                obj.upper_limit = data.get('upper_limit', obj.upper_limit)
                obj.lower_limit = data.get('lower_limit', obj.lower_limit)
                obj.is_limit = data.get('is_limit', obj.is_limit)
                obj.limit_time = data.get('limit_time', obj.limit_time)
                obj.activity_state = data.get('activity_state', obj.activity_state)
                obj.is_irres = data.get('is_irres',obj.is_irres)
                obj.irres_time = data.get('irres_time',obj.irres_time)
                obj.save()
                serializer = Act_info(obj, many=False)
                return JSONResponse(0,serializer.data)
        except Exception as a:
            return JSONResponse(1000)
    else:
        return JSONResponse(1057)



@csrf_exempt
def Activity_delete(request):
    '''
    删除指定活动
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            obj = QyActivity.objects.get(pk=data.get('pk'))
            if obj.activity_state is not 3:
                with transaction.atomic():
                    # obj.delete()
                    obj.activity_state=3
                    obj.save()
            return JSONResponse(0)
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1056)



@csrf_exempt
def Activity_filter(request):
    '''
    筛选活动
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            address_detailed = request.GET.get('address_detailed')
            formater = request.GET.get('formater')
            type = request.GET.get('type')
            org_nickname = request.GET.get('org_nickname')
            if address_detailed and (not formater) and (not type):
                obj = QyActivity.objects.filter(
                    address_detailed__contains=address_detailed,
                    activity_state__lte=2).order_by('-id')
            elif org_nickname and (not formater) and (not type):
                originator_id = []
                originator = QyMember.objects.filter(
                    nickname__contains=request.GET.get('org_nickname'))
                for ori in originator:
                    originator_id.append(ori.id)
                obj = QyActivity.objects.filter(
                    originator_id__in=originator_id,
                    activity_state__lte=2).order_by('-id')
            elif formater and (not address_detailed) \
                    and (not type) and (not org_nickname):
                obj = QyActivity.objects.filter(
                    formater=formater,activity_state__lte=2).order_by('-id')
            elif type and (not formater) and (not address_detailed) \
                    and (not org_nickname):
                obj = QyActivity.objects.filter(
                    type=type,activity_state__lte=2).order_by('-id')
            elif address_detailed and formater and (not type):
                obj = QyActivity.objects.filter(
                    address_detailed__contains=address_detailed,
                    formater=formater,activity_state__lte=2).order_by('-id')
            elif address_detailed and type and (not formater):
                obj = QyActivity.objects.filter(
                    address_detailed__contains=address_detailed,
                    type=type,activity_state__lte=2).order_by('-id')
            elif org_nickname and formater and (not type):
                originator_id = []
                originator = QyMember.objects.filter(
                    nickname__contains=request.GET.get('org_nickname'))
                for ori in originator:
                    originator_id.append(ori.id)
                obj = QyActivity.objects.filter(
                    originator_id__in=originator_id,formater=formater,
                    activity_state__lte=2).order_by('-id')
            elif org_nickname and type and (not formater):
                originator_id = []
                originator = QyMember.objects.filter(
                    nickname__contains=request.GET.get('org_nickname'))
                for ori in originator:
                    originator_id.append(ori.id)
                obj = QyActivity.objects.filter(
                    originator_id__in=originator_id,type=type,
                    activity_state__lte=2).order_by('-id')
            elif formater and type and (not address_detailed) \
                    and (not org_nickname):
                obj = QyActivity.objects.filter(
                    formater=formater,type=type,
                    activity_state__lte=2).order_by('-id')
            elif formater and type and address_detailed:
                obj = QyActivity.objects.filter(
                    address_detailed__contains=address_detailed,
                    formater=formater,type=type,
                    activity_state__lte=2).order_by('-id')
            elif formater and type and org_nickname:
                originator_id = []
                originator = QyMember.objects.filter(
                    nickname__contains=request.GET.get('org_nickname'))
                for ori in originator:
                    originator_id.append(ori.id)
                obj = QyActivity.objects.filter(
                    originator_id__in=originator_id,
                    type=type,formater=formater,
                    activity_state__lte=2).order_by('-id')
            else:
                obj = QyActivity.objects.filter(
                    activity_state__lte=2).order_by('-id')
            # 进行分页
            pag = mypage(request.GET.get('page'), obj)
            serializer = Act_info(pag['page_list'], many=True)
            return JSONResponse(0, serializer.data, pag['page_sum'], pag['page_count'])
        except:
            return JSONResponse(1007)





@csrf_exempt
def file(request):
    '''
    文件上传
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = request.FILES.getlist('img')
            img = MyFile().mybase64(data)
            return JSONResponse(0,img)
        except:
            return JSONResponse(1007)




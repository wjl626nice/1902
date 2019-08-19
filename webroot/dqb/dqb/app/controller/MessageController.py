from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from app.model.MessageModel import MessageSerializers,QyMessage
from app.model.MemberModel import QyMember
from app.model.ReplayModel import QyReply
from base.myjson import JSONResponse
from base.my_page import mypage
import json
import time



@csrf_exempt
def getMessageAll(request):
    '''
    所有与指定活动相关的留言及回复
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            page = request.GET.get('page')
            activity_id = request.GET.get('activity')
            objs = QyMessage.objects.filter(activity=activity_id)

            p = mypage(page, objs)
            obj = p['page_list']
            total = p['page_sum']

            serializer = MessageSerializers(obj,many=True)
            return JSONResponse(0,serializer.data,total)
        except Exception as e:
            return JSONResponse(1001)
    else:
        return JSONResponse(1054)



@csrf_exempt
def createMessage(request):
    '''
    用户创建留言
    :param request:
    :return:
    '''
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            with transaction.atomic():

                member_id = QyMember.objects.get(openid=data.get('openid')).id
                if not data.get('activity_id'):
                    return JSONResponse(1007)
                obj = QyMessage(
                    activity = data.get('activity_id'),
                    member_id= member_id,
                    message_content = data.get('message_content'),
                    message_img = data.get('message_img'),
                    add_time = str(int(time.time()))
                )
                obj.save()
                return JSONResponse(0)
        except Exception as e:
            return JSONResponse(1001)
    else:
        return JSONResponse(1055)




@csrf_exempt
def delete_message(request):
    '''
    删除留言
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message_id = data.get('message')
            QyMessage.objects.get(pk=message_id).delete()
            QyReply.objects.filter(message_id = message_id).delete()
            return JSONResponse(0)
        except:
            return JSONResponse(1001)
    else:
        return JSONResponse(1055)
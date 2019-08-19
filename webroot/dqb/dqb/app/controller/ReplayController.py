from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from base.myjson import JSONResponse
from app.model.ReplayModel import QyReply,ReplaySerializer
from app.model.MemberModel import QyMember
import json,time



@csrf_exempt
def get_replyAll(request):
    '''
    查询指定留言下的所有回复
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            message_id = request.GET.get('message')
            objs = QyReply.objects.filter(message_id=message_id)
            serializer = ReplaySerializer(objs,many=True)
            return JSONResponse(0,serializer.data)
        except:
            return JSONResponse(1001)
    else:
        return JSONResponse(1054)



@csrf_exempt
def create_reply(request):
    '''
    创建回复信息
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            reply_member_id = QyMember.objects.get(openid=data.get('reply_openid')).id
            with transaction.atomic():
                obj = QyReply(
                    reply_content = data.get('reply_content'),
                    message_id = data.get('message_id'),
                    reply_member = reply_member_id,
                    to_reply_member = data.get('to_reply_member'),
                    add_time = str(int(time.time()))
                )
                obj.save()
                return JSONResponse(0)
        except:
            return JSONResponse(1001)
    else:
        return JSONResponse(1055)
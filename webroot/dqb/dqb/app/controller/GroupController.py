from app.model.MemberModel import QyMember,MemberSerializer
from django.views.decorators.csrf import csrf_exempt
from app.model.GroupModel import MyGroup,QyGroup
from base.myjson import JSONResponse
from app.model.NewsModel import QyNews
import json,time



@csrf_exempt
def create_myfriends(request):
    '''
    同意/拒绝添加球友
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # 判断是否已同意 如果同意就添加球友
            try:
                news = QyNews.objects.get(pk=data.get('id'))
            except:
                return JSONResponse(1010)

            # 判断是否已同意 如果同意就添加球友
            if data.get('new_state') == 1:
                news.new_state = data.get('new_state')
                news.save()

                # 判断是否已经为球友关系
                friend = QyGroup.objects.filter(member_a_id=news.applicant_id,member_b_id=news.respondent_id)
                # 如果是球友返回，不是创建
                if friend:
                    return JSONResponse(1008)

                obj_a = QyGroup(
                    member_a_id = news.applicant_id,
                    member_b_id = news.respondent_id,
                    add_time = str(int(time.time()))
                )
                obj_b = QyGroup(
                    member_a_id=news.respondent_id,
                    member_b_id=news.applicant_id,
                    add_time=str(int(time.time()))
                )
                obj_a.save()
                obj_b.save()
                return JSONResponse(0)
            elif data.get('new_state') == 0:
                news.new_state = data.get('new_state')
                news.save()
                return JSONResponse(1009)
            else :
                return JSONResponse(1001)
        except:
            return JSONResponse(1001)
    else:
        return JSONResponse(1055)



@csrf_exempt
def delete_myfriends(request):
    '''
    删除球友
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            QyGroup.objects.get(member_a_id=data.get('member_a_id'),member_b_id=data.get('member_b_id')).delete()
            QyGroup.objects.get(member_b_id=data.get('member_a_id'),member_a_id=data.get('member_b_id')).delete()
            return JSONResponse(0)
        except:
            return JSONResponse(1057)
    else:
        JSONResponse(1055)



@csrf_exempt
def myGroup(request):
    '''
    查询'我'的球友
    :param request:
    :return:
    '''
    if request.method == 'GET':
        myId = request.GET.get('member_a')
        if myId:
            try:
                objs = QyGroup.objects.filter(member_a_id=myId)
                serializer = MyGroup(objs,many=True)
                return JSONResponse(0,serializer.data)
            except Exception as e:
                return JSONResponse(1001)
        else:
            return JSONResponse(1001)
    else:
        return JSONResponse(1054)



@csrf_exempt
def up_myGroup(request):
    '''
    修改'球友'分组/标签
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            g = QyGroup.objects.get(member_a_id=data['member_a_id'],member_b_id=data['member_b_id'])
            g.group = data.get('group',g.group)
            g.save()
            return JSONResponse(0)
        except:
            return JSONResponse(1001)
    else:
        return JSONResponse(1057)



@csrf_exempt
def common_friend(request):
    '''
    查询'共同球友'
    :param request:
    :return:
    '''
    if request.method == 'GET':
        member_id = request.GET.get('member')
        friend_id = request.GET.get('friend')
        try:
            # 分别取出各自的好友
            m = QyGroup.objects.filter(member_a_id=member_id)
            m_friends = []
            for x in m:
                m_friends.append(x.member_b_id)

            f = QyGroup.objects.filter(member_a_id=friend_id)
            f_friends = []
            for y in f:
                f_friends.append(y.member_b_id)

            # 获取他们的交集
            common = [i for i in m_friends if i in f_friends]

            common_friends = []
            for member in common:
                common_friends.append(QyMember.objects.get(pk=member))

            serializer = MemberSerializer(common_friends, many=True)
            return JSONResponse(0,serializer.data)
        except:
            return JSONResponse(1001)
    else:
        return JSONResponse(1054)
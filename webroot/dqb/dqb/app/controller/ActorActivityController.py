from base.myjson import JSONResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from app.model.ActorActivityModel import QyActor_activities
from app.model.MemberModel import QyMember,Member_feedback
from app.model.ActivityModel import QyActivity,Act_info
from app.model.GroupModel import QyGroup
from app.model.PayModel import QyPay
from base.my_page import mypage
from base.mysort import my_sort,time_stamp
import json
import time

# Create your views here.


@csrf_exempt
def my_historical_act(request):
    '''
    我的历史活动
    :param request: openid
    :return:
    '''
    if request.method == 'GET':
        try:
            openid = request.GET.get('openid')
            member_id = QyMember.objects.get(openid=openid).id

            # 我组织的活动
            my_objs = QyActivity.objects.filter(originator_id=member_id)
            act_id = []
            for x in my_objs:
                act_id.append(x.id)

            # 我参加的活动
            objs = QyActor_activities.objects.filter(member_id=member_id)
            objs_act = []
            for y in objs:
                objs_act.append(y.activity_id)

            # 取并集
            act = list(set(act_id).union(set(objs_act)))
            # 我的历史活动
            activities = QyActivity.objects.filter(
                pk__in=act,activity_state=2).order_by('-id')

            # 分页
            pag = mypage(request.GET.get('page'), activities)
            # 序列化
            serializer = Act_info(pag['page_list'],many=True)
            return JSONResponse(0,serializer.data)
        except Exception as e:
            return JSONResponse(1007)

@csrf_exempt
def Activity_my_list(request):
    '''
    获得我参加过的所有活动列表
    :param request:openid
    :return:
    '''
    if request.method == 'GET':
        try:
            member_id = QyMember.objects.get(
                openid=request.GET.get('openid')).id
            objs = QyActor_activities.objects.filter(
                member_id=member_id,reg_state=1)
            objs_act = []
            for y in objs:
                objs_act.append(y.activity_id)
            obj = QyActivity.objects.filter(
                pk__in=objs_act,activity_state=2)
            pag = mypage(request.GET.get('page'), obj)
            serializer = Act_info(pag['page_list'],many=True)
            return JSONResponse(0,serializer.data,pag['page_sum'])
        except Exception as q:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)



@csrf_exempt
def myParticipatingActivity(request):
    '''
    首页 我已报名的且未过期或已取消的活动详情
    :param request:openid,sort,address
    :return:
    '''
    if request.method == 'GET':
        try:
            openid = request.GET.get('openid')
            sort = request.GET.get('sort')
            member_id = QyMember.objects.get(openid=openid).id

            # 我组织的活动
            my_objs = QyActivity.objects.filter(originator_id=member_id)
            act_id = []
            for x in my_objs:
                act_id.append(x.id)

            # 我参加的活动
            objs = QyActor_activities.objects.filter(member_id=member_id)
            objs_act = []
            for y in objs:
                objs_act.append(y.activity_id)

            # 取并集
            act = list(set(act_id).union(set(objs_act)))

            # 筛选其中没有过期的活动
            activities_id = []
            for x in act:
                obj = QyActivity.objects.filter(pk=x,activity_state__lte=1)
                if obj:
                    activities_id.append(obj[0].id)

            # 对筛选过的活动排序
            if sort == '3':
                address = request.GET.get('address')
                activities = QyActivity.objects.filter(
                    pk__in=activities_id,
                    address_detailed__contains=address)
            else:
                activities = QyActivity.objects.filter(
                    pk__in=activities_id).order_by(my_sort(sort))

            # 分页
            pag = mypage(request.GET.get('page'), activities)
            # 序列化
            serializer = Act_info(pag['page_list'],many=True)
            return JSONResponse(0,serializer.data)
        except Exception as e:
            return JSONResponse(1007)



@csrf_exempt
def Activity_signup(request):
    '''
    报名指定活动/修改报名状态
    :param request:
    :return:
    '''
    if request.method == 'POST':
        try:
            with transaction.atomic():
                data = json.loads(request.body)
                act = QyActivity.objects.filter(
                    pk=data.get('activity_id'),
                    activity_state=1)
                if act:
                    member = QyMember.objects.get(
                        openid=data.get('openid'))
                    is_signup = QyActor_activities.objects.filter(
                        activity_id=data.get('activity_id'),
                        member_id=member.id)
                    # 判断是否有报名参与过指定的活动（没参与过创建参与）
                    if not is_signup:
                            obj = QyActor_activities(
                                activity_id=data.get('activity_id'),
                                member_id = member.id,
                                reg_state =data.get('reg_state'),
                                add_time = str(int(time.time()))
                            )
                            if data.get('reg_state') > 1:
                                obj.save()
                            elif data.get('reg_state') == 1 \
                                    and eval(member.balance) \
                                    >= eval(act[0].price):
                                if eval(act[0].price) > 0:
                                    member.balance = "%.2f" % (eval(member.balance)
                                                               - eval(act[0].price))
                                    member.save()
                                    pay = QyPay(member_id=member.id,pay_type=4,
                                                pay_amount=act[0].price,
                                                pay_state=3,
                                                add_time=str(int(time.time())))
                                    pay.save()
                                obj.save()
                            else:
                                return JSONResponse(2003)
                    # 判断参与的活动自己所处状态是否和本次修改一致（不一致进行更改）
                    elif not data.get('reg_state') == is_signup[0].reg_state:
                        if (is_signup[0].reg_state is not 1) \
                                and (not data.get('reg_state') == 1):
                            is_signup[0].reg_state = data.get('reg_state')
                            is_signup[0].save()
                        elif is_signup[0].reg_state == 1:
                            if eval(act[0].price) > 0:
                                member.balance = "%.2f" % (eval(member.balance)
                                                           + eval(act[0].price))
                                member.save()
                                pay = QyPay(member_id=member.id, pay_type=3,
                                            pay_amount=act[0].price,
                                            pay_state=3,
                                            add_time=str(int(time.time())))
                                pay.save()
                            is_signup[0].reg_state = data.get('reg_state')
                            is_signup[0].save()
                        elif (data.get('reg_state') == 1) \
                                and (eval(member.balance) >= eval(act[0].price)):
                            if eval(act[0].price) > 0:
                                member.balance = "%.2f" % (eval(member.balance)
                                                           - eval(act[0].price))
                                member.save()
                                pay = QyPay(member_id=member.id, pay_type=4,
                                            pay_amount=act[0].price,
                                            pay_state=3,
                                            add_time=str(int(time.time())))
                                pay.save()
                            is_signup[0].reg_state = data.get('reg_state')
                            is_signup[0].save()
                        else:
                            return JSONResponse(2003)
                    else:
                        return JSONResponse(1001)
                    objs = QyMember.objects.filter(pk=member.id)
                    serializer = Member_feedback(objs, many=True)
                    return JSONResponse(0,serializer.data)
                else:
                    return JSONResponse(1000)
        except Exception as e:
            return JSONResponse(1007)
    else:
        return JSONResponse(1057)



@csrf_exempt
def Activity_delete(request):
    '''
    取消报名指定活动
    :param request:
    :return:
    '''
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            act = QyActivity.objects.filter(
                    pk=data.get('activity_id'),
                    activity_state=1)
            if act:
                with transaction.atomic():
                    member = QyMember.objects.get(
                        openid=data.get('openid'))
                    is_signup = QyActor_activities.objects.get(
                        activity_id=data.get('activity_id'),
                        member_id=member.id)
                    if is_signup.reg_state == 1:
                        if (act[0].is_irres == 0) \
                                or ((act[0].is_irres == 1)
                                    and (int(act[0].irres_time) > int(time.time()))):
                            if eval(act[0].price) > 0:
                                member.balance = "%.2f" % (eval(member.balance)
                                                           + eval(act[0].price))
                                member.save()
                                pay = QyPay(member_id=member.id, pay_type=3,
                                            pay_amount=act[0].price,
                                            pay_state=3,
                                            add_time=str(int(time.time())))
                                pay.save()
                    is_signup.delete()
                    return JSONResponse(0)
            else:
                return JSONResponse(1000)
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1056)



@csrf_exempt
def recommend_activity(request):
    '''
    推荐的活动列表
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            openid = request.GET.get('openid')
            my_id = QyMember.objects.get(openid=openid).id

            # 查询 所有不是本人举办的且状态为可参加的活动
            objs_notOriginator = QyActivity.objects.filter(
                activity_state=1).exclude(originator_id=my_id)

            notOriginator = []
            for x in objs_notOriginator:
                notOriginator.append(x.id)

            # 获取其中 本人没有参与的活动
            notActor = []
            for y in notOriginator:
                actor_activity = QyActor_activities.objects.filter(
                    activity_id=y, member_id=my_id)
                if not actor_activity:
                    notActor.append(y)

            # 获取其中 活动状态为可参加的 并排序
            sort = request.GET.get('sort')
            address = request.GET.get('address')
            activity_time = request.GET.get('activity_time')
            formater = request.GET.get('formater')

            # 地点
            if sort == '3':
                objs = QyActivity.objects.filter(
                    pk__in=notActor, activity_state=1,
                    address_detailed__contains=address
                )
            # 时间
            elif sort == '1':
                objs = QyActivity.objects.filter(
                    pk__in=notActor, activity_state=1,
                    activity_time__gte=time_stamp(activity_time).get('star'),
                    activity_time__lte=time_stamp(activity_time).get('end')
                )
            # 赛制
            elif sort == '2':
                objs = QyActivity.objects.filter(
                    pk__in=notActor, activity_state=1,
                    formater = formater
                    )
            else:
                objs = QyActivity.objects.filter(
                    pk__in=notActor, activity_state=1
                ).order_by(my_sort(sort))

            # 判断活动类别是 散踢(可见)/队内(与origin为好友可见)
            objs_actor = []
            for obj in objs:
                if obj.type == 0:
                    objs_actor.append(obj)
                elif obj.type == 1:
                    friend = QyGroup.objects.filter(
                        member_a_id=obj.originator_id,
                        member_b_id=my_id)
                    if friend:
                        objs_actor.append(obj)
                    else:
                        pass
                else:
                    pass
            pag = mypage(request.GET.get('page'), objs_actor)
            serializer = Act_info(pag['page_list'], many=True)
            return JSONResponse(0,serializer.data)
        except Exception as e:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)

@csrf_exempt
def act_user(request):
    '''
    踢过球的人列表
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            openid = request.GET.get('openid')
            my_id = QyMember.objects.get(openid=openid).id
            objs = QyActor_activities.objects.filter(member_id=my_id)
            act_list = []
            for obj in objs:
                act_list.append(obj.activity_id)
            ac_list = []
            obj = QyActivity.objects.filter(pk__in=act_list,activity_state=2)
            for ob in obj:
                ac_list.append(ob.id)
            obs = QyActor_activities.objects.filter(activity_id__in=ac_list)
            meb_list = []
            for ob in obs:
                if ob.member_id is not my_id:
                    meb_list.append(ob.member_id)
            obj = QyMember.objects.filter(pk__in=meb_list).distinct()
            pag = mypage(request.GET.get('page'), obj)
            serializer = Member_feedback(pag['page_list'], many=True)
            return JSONResponse(0,serializer.data)
        except:
            return JSONResponse(1007)


@csrf_exempt
def act_user_sum(request):
    '''
    踢过球的人数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        try:
            openid = request.GET.get('openid')
            my_id = QyMember.objects.get(openid=openid).id
            objs = QyActor_activities.objects.filter(member_id=my_id)
            act_list = []
            for obj in objs:
                act_list.append(obj.activity_id)
            ac_list = []
            obj = QyActivity.objects.filter(pk__in=act_list,activity_state=2)
            for ob in obj:
                ac_list.append(ob.id)
            obs = QyActor_activities.objects.filter(activity_id__in=ac_list)
            meb_list = []
            for ob in obs:
                if ob.member_id is not my_id:
                    meb_list.append(ob.member_id)
            return JSONResponse(0,{'sum':len(set(meb_list))})
        except:
            return JSONResponse(1007)


@csrf_exempt
def Act_sum(request):
    '''
    踢球总次数
    :param request:openid
    :return:
    '''
    if request.method == 'GET':
        try:
            member_id = request.GET.get('id')
            objs = QyActor_activities.objects.filter(
                member_id=member_id,reg_state=1)
            objs_act = []
            for y in objs:
                objs_act.append(y.activity_id)
            obj = len(QyActivity.objects.filter(
                pk__in=objs_act,activity_state=2))

            return JSONResponse(0,{"sum":obj})
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)


@csrf_exempt
def together_ball(request):
    '''
    我与指定用户一起踢过球总数
    :param request:openid
    :return:
    '''
    if request.method == 'GET':
        try:
            member_id = QyMember.objects.get(
                openid=request.GET.get('openid')).id
            objs_a = QyActor_activities.objects.filter(
                member_id=member_id,reg_state=1)
            objs_act = []
            for y in objs_a:
                objs_act.append(y.activity_id)
            objs_b = QyActor_activities.objects.filter(
                member_id=request.GET.get('id'), reg_state=1)
            for y in objs_b:
                objs_act.append(y.activity_id)

            obj = len(QyActivity.objects.filter(
                pk__in=list(set(objs_act)),activity_state=2))
            return JSONResponse(0,{'sum':obj})
        except:
            return JSONResponse(1007)
    else:
        return JSONResponse(1054)


def Activity_over():
    '''
    监控活动过期状态，超过举办时间自动过期
    '''
    try:
        with transaction.atomic():
            objs_a = QyActivity.objects.filter(
                activity_state=1,is_limit=1,
                limit_time__lte=time.time())
            if objs_a:
                for obj in objs_a:
                    bm = QyActor_activities.objects.filter(
                        activity_id=obj.id, reg_state=1)
                    if obj.lower_limit > len(bm):
                        obj.activity_state = 0
                        for b in bm:
                            us = QyMember.objects.get(pk=b.member_id)
                            act = QyActivity.objects.get(pk=b.activity_id)
                            if eval(act.price) > 0:
                                us.balance = "%.2f" % (eval(us.balance)
                                                           + eval(act.price))
                                us.save()
                                pay = QyPay(member_id=us.id, pay_type=3,
                                            pay_amount=act.price,
                                            pay_state=3,
                                            add_time=str(int(time.time())))
                                pay.save()
                        obj.save()

            objs_b = QyActivity.objects.filter(
                activity_state=1,
                activity_time__lte=time.time())
            if objs_b:
                for obj in objs_b:
                    bm = QyActor_activities.objects.filter(
                        activity_id=obj.id,reg_state=1)
                    if (obj.is_limit is 0) and (obj.lower_limit > len(bm)):
                        obj.activity_state = 0
                        for b in bm:
                            us = QyMember.objects.get(pk=b.member_id)
                            act = QyActivity.objects.get(pk=b.activity_id)
                            if eval(act.price) > 0:
                                us.balance = "%.2f" % (eval(us.balance)
                                                           + eval(act.price))
                                us.save()
                                pay = QyPay(member_id=us.id, pay_type=3,
                                            pay_amount=act.price,
                                            pay_state=3,
                                            add_time=str(int(time.time())))
                                pay.save()
                    else:
                        obj.activity_state = 2
                        for b in bm:
                            act = QyActivity.objects.get(pk=b.activity_id)
                            us = QyMember.objects.get(pk=act.originator_id)
                            act_us = len(QyActor_activities.objects.filter(
                                activity_id=act.id,reg_state=1))
                            if eval(act.price) > 0:
                                us.balance = "%.2f" % (eval(us.balance)
                                                           + eval(act.price)*act_us)
                                us.save()
                                pay = QyPay(member_id=us.id, pay_type=5,
                                            pay_amount=eval(act.price)*act_us,
                                            pay_state=3,
                                            add_time=str(int(time.time())))
                                pay.save()
                    obj.save()
    except Exception as e:
        pass



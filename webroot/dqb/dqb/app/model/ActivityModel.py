# coding=utf-8

from django.db import models
from app.model.MemberModel import QyMember,MemberSerializer
from app.model.ActorActivityModel import QyActor_activities,ActorActivitySerializer
from rest_framework.serializers import SerializerMethodField,ModelSerializer


# 活动表
class QyActivity(models.Model):
    saizhi = (
        (0, '待定'),
        (1, '5人制'),
        (2, '6人制'),
        (3, '7人制'),
        (4, '8人制'),
        (5, '9人制'),
        (6, '10人制'),
        (7, '11人制')
    )
    activity_type = (
        (0,'散踢'),
        (1,'队内活动'),
        (2,'球队比赛')
    )
    timeLimit = (
        (0, '不限时'),
        (1, '限时')
    )
    state = (
        (0, '已取消'),
        (1, '可参加'),
        (2, '已过期')
    )
    notice = models.TextField('公告',blank=True)
    activity_time = models.CharField('活动时间',blank=True,max_length=20)
    address_province = models.CharField('省份', max_length=20, blank=True)
    address_city = models.CharField('城市', max_length=20, blank=True)
    address_area = models.CharField('区/县', max_length=20, blank=True)
    address_detailed = models.CharField('详细地点',blank=True,max_length=256)
    formater = models.IntegerField('赛制',
                                   choices=saizhi,
                                   default=0
                                   )
    type = models.IntegerField('类型',
                                    choices=activity_type,
                                    default=0
                                    )
    upper_limit = models.IntegerField('人数上限',blank=True)
    lower_limit = models.IntegerField('人数下限',blank=True)
    is_limit = models.IntegerField('是否设置限时报名',
                                  choices=timeLimit,
                                  default=0
                                  )
    limit_time = models.CharField('报名截止时间',max_length=20,blank=True)
    price = models.CharField('报名费用',default='0.00',max_length=16)
    activity_img = models.TextField('活动图片',max_length=255,blank=True)
    originator_id = models.IntegerField('发起人')
    activity_state = models.IntegerField('活动状态',
                                         choices=state,
                                         default=1
                                         )
    add_time = models.CharField('创建时间',max_length=20)
    is_irres = models.IntegerField('是否限时无责',
                                         choices=((0, '不限时'),(1, '限时')),
                                         default=0
                                         )
    irres_time = models.CharField('无责时间',max_length=20,blank=True)


    class Meta:
        db_table = 'qy_activity'
        verbose_name = '活动'
        verbose_name_plural = verbose_name


# 活动详情
class Act_info(ModelSerializer):
    originator_id = SerializerMethodField()
    participant = SerializerMethodField()
    leave = SerializerMethodField()
    undetermined = SerializerMethodField()
    is_Pay = SerializerMethodField()

    class Meta:
        model = QyActivity
        exclude = ('address_province','address_city','address_area')

    # 活动发起人员信息
    def get_originator_id(self, obj):
        originator = QyMember.objects.get(pk=obj.originator_id)
        originatorS = MemberSerializer(originator, many=False)
        return originatorS.data

    # 报名人员信息列表
    def get_participant(self,obj):
        act = QyActor_activities.objects.filter(activity_id=obj.id,reg_state=1)
        acts = ActorActivitySerializer(act,many=True)
        return acts.data

    # 待定人员信息列表
    def get_undetermined(self,obj):
        act = QyActor_activities.objects.filter(activity_id=obj.id,reg_state=2)
        acts = ActorActivitySerializer(act,many=True)
        return acts.data

    # 请假人员信息列表
    def get_leave(self,obj):
        act = QyActor_activities.objects.filter(activity_id=obj.id,reg_state=3)
        acts = ActorActivitySerializer(act,many=True)
        return acts.data

    # 付费人员信息列表
    def get_is_Pay(self,obj):
        act = QyActor_activities.objects.filter(activity_id=obj.id,free_state=0)
        acts = ActorActivitySerializer(act,many=True)
        return acts.data


# 我参加的活动
class Activity_my(ModelSerializer):
    member_id = SerializerMethodField()
    activity_id = SerializerMethodField()
    class Meta:
        model = QyActor_activities
        fields = ('reg_state','free_state','activity_id','member_id')

    # 参加人员信息
    def get_member_id(self, obj):
        member = QyMember.objects.get(pk=obj.member_id)
        members = MemberSerializer(member, many=False)
        return members.data

    # 参加的活动信息
    def get_activity_id(self, obj):
        act = QyActivity.objects.get(pk=obj.activity_id)
        acts = Act_info(act, many=False)
        return acts.data


# 首页 我已报名的且未过期的活动
class MyParticipating(ModelSerializer):
    actor = SerializerMethodField()
    originator_id = SerializerMethodField()

    class Meta:
        model = QyActivity
        exclude = ('address_province','address_city','address_area')

    def get_originator_id(self, obj):
        originator = QyMember.objects.get(pk=obj.originator_id)
        originatorS = MemberSerializer(originator, many=False)
        return originatorS.data

    def get_actor(self,obj):
        actor_activity = QyActor_activities.objects.filter(activity_id=obj.id)
        actor = []
        for x in actor_activity:
            member = QyMember.objects.get(pk=x.member_id)
            actor.append(member)
        actorS = MemberSerializer(actor, many=True)
        return actorS.data
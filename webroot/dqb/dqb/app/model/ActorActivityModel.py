# coding=utf-8

from django.db import models
from app.model.MemberModel import QyMember,MemberSerializer
from rest_framework.serializers import ModelSerializer,SerializerMethodField




# 参加人员表(类中间表)
class QyActor_activities(models.Model):
    regState = (
        (1, '报名'),
        (2, '待定'),
        (3, '请假')
    )
    freeState = (
        (0, '付费'),
        (1, '免费')
    )
    activity_id = models.IntegerField()
    member_id = models.IntegerField()
    reg_state = models.IntegerField('参加人员状态',
                                         choices=regState,
                                         default=2
                                         )
    free_state = models.IntegerField('是否付费',
                                     choices=freeState,
                                     default=0
                                     )
    add_time = models.CharField('创建时间',max_length=20)

    class Meta:
        db_table = 'qy_actor_activities'
        verbose_name = '用户-活动中间表'
        verbose_name_plural = verbose_name


# 参加人员
class ActorActivitySerializer(ModelSerializer):
    member_id = SerializerMethodField()
    class Meta:
        model = QyActor_activities
        fields = ('member_id','reg_state','free_state')

    # 参加人员信息
    def get_member_id(self, obj):
        member = QyMember.objects.get(pk=obj.member_id)
        members = MemberSerializer(member, many=False)
        return members.data



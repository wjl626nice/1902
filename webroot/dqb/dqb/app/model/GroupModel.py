# coding=utf-8
from app.model.MemberModel import QyMember,Member_feedback
from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


# 标签/分组表
class QyGroup(models.Model):
    member_a_id = models.IntegerField("用户")
    member_b_id = models.IntegerField("被打标签用户")
    group = models.CharField('分组',max_length=32,default='我的球友')
    add_time = models.CharField('创建时间', max_length=20)

    class Meta:
        db_table = 'qy_group'


# 标签/分组实体类
class MyGroup(ModelSerializer):
    member_b_id = serializers.SerializerMethodField()

    class Meta:
        model = QyGroup
        fields = ('member_b_id','group')

    def get_member_b_id(self,obj):

        member = QyMember.objects.get(pk=obj.member_b_id)
        memberS = Member_feedback(member,many=False)
        return memberS.data
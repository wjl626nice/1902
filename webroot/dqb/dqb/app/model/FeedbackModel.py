from app.model.MemberModel import QyMember,Member_feedback
from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


# 意见反馈表
class QyFeedback(models.Model):
    feedState = (
        (0, '未查看'),
        (1, '已查看')
    )
    member_id = models.IntegerField("用户id",blank=True)
    content = models.TextField('反馈的意见内容',blank=True)
    Feedback_state = models.IntegerField('是否已查看',choices=feedState,default=0)
    add_time = models.CharField('创建时间', max_length=20,blank=True)

    class Meta:
        db_table = 'qy_Feedback'


# 标签/分组实体类
class Feedback(ModelSerializer):
    member_id = serializers.SerializerMethodField()

    class Meta:
        model = QyFeedback
        fields = '__all__'

    def get_member_id(self,obj):

        member = QyMember.objects.get(pk=obj.member_id)
        memberS = Member_feedback(member,many=False)
        return memberS.data
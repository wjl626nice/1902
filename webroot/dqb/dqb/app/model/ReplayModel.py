# coding=utf-8

from django.db import models
from app.model.MemberModel import QyMember,MemberSerializer
from rest_framework.serializers import SerializerMethodField,ModelSerializer


# 回复
class QyReply(models.Model):
    message_id = models.IntegerField('关联的留言ID')
    reply_member = models.IntegerField('回复人')
    to_reply_member = models.IntegerField('被回复者')
    reply_content = models.TextField('回复内容',blank=True)
    add_time = models.CharField('创建时间',max_length=20)

    class Meta:
        db_table = 'qy_replay'


# 回复实体类
class ReplaySerializer(ModelSerializer):
    reply_member = SerializerMethodField()
    to_reply_member = SerializerMethodField()

    class Meta:
        model = QyReply
        fields = '__all__'

    def get_reply_member(self,obj):
        reply_member = QyMember.objects.get(pk=obj.reply_member)
        reply_memberS = MemberSerializer(reply_member, many=False)

        return reply_memberS.data

    def get_to_reply_member(self,obj):
        to_reply_member = QyMember.objects.get(pk=obj.to_reply_member)

        to_reply_memberS = MemberSerializer(to_reply_member, many=False)
        return to_reply_memberS.data
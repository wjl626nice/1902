# coding=utf-8

from django.db import models
from app.model.MemberModel import QyMember,MemberSerializer
from app.model.ReplayModel import QyReply,ReplaySerializer
from rest_framework.serializers import ModelSerializer,SerializerMethodField


# 留言
class QyMessage(models.Model):
    activity = models.IntegerField('相关活动ID')
    member_id = models.IntegerField('留言人')
    message_img = models.TextField('留言图片',max_length=255,blank=True)
    message_content = models.TextField('留言内容',blank=True)
    add_time = models.CharField('创建时间', max_length=20)

    class Meta:
        db_table = 'qy_message'
        verbose_name = '留言'
        verbose_name_plural = verbose_name


# 留言实体类
class MessageSerializers(ModelSerializer):

    member_id = SerializerMethodField()
    replay = SerializerMethodField()

    class Meta:
        model = QyMessage
        fields = '__all__'

    def get_member_id(self,obj):
        member = QyMember.objects.get(pk=obj.member_id)
        memberS = MemberSerializer(member,many=False)
        return memberS.data

    def get_replay(self,obj):
        objs = QyReply.objects.filter(message_id=obj.id)
        serializer = ReplaySerializer(objs, many=True)
        return serializer.data
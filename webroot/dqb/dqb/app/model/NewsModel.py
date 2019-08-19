# coding=utf-8

from django.db import models
from rest_framework.serializers import SerializerMethodField,ModelSerializer
from app.model.MemberModel import QyMember,MemberSerializer


# Create your models here.


# 申请添加球友
class QyNews(models.Model):
    newState = (
        (0, '拒绝'),
        (1, '同意'),
        (2, '待处理')
    )
    applicant_id = models.IntegerField('申请人')
    respondent_id = models.IntegerField('被申请人')
    content = models.TextField('消息内容',blank=True)
    apply_time = models.CharField('申请时间',max_length=20)
    new_state = models.IntegerField('消息状态',choices=newState,default=2)

    class Meta:
        db_table = 'qy_news'
        verbose_name = '消息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content



# 获取申请人具体信息
class News_getApplicant(ModelSerializer):
    applicant = SerializerMethodField()

    class Meta:
        model = QyNews
        fields = '__all__'

    def get_applicant(self,obj):
        member = QyMember.objects.get(pk=obj.applicant_id)
        memberS = MemberSerializer(member,many=False)
        return memberS.data


# 获取被申请人具体信息
class News_getRespondent(ModelSerializer):
    respondent = SerializerMethodField()

    class Meta:
        model = QyNews
        fields = '__all__'

    def get_respondent(self,obj):
        member = QyMember.objects.get(pk=obj.respondent_id)
        memberS = MemberSerializer(member,many=False)
        return memberS.data
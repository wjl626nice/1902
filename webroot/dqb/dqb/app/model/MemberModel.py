from django.db import models
from rest_framework.serializers import ModelSerializer

# Create your models here.


# 用户
class QyMember(models.Model):
    openid = models.CharField('openid', max_length=30,blank=True)
    unionid = models.CharField('unionid', max_length=30,blank=True)
    avatar = models.TextField('头像',max_length=255,blank=True)
    age = models.IntegerField('年龄',blank=True)
    nickname = models.CharField('昵称',blank=True,max_length=56)
    profession = models.CharField('职业',blank=True,max_length=255)
    phonenum = models.BigIntegerField('电话',blank=True)
    balance = models.CharField('余额',blank=True,max_length=20,default='0.00')
    add_time = models.CharField('创建时间', max_length=20)
    cardholder = models.CharField('持卡人',blank=True,max_length=56)
    ID_number = models.CharField('身份证号',blank=True,max_length=20)
    opening_bank = models.CharField('开户行',blank=True,max_length=36)
    bank_card_number = models.CharField('银行卡号',blank=True,max_length=22)
    reserved_phone_number = models.BigIntegerField('银行预留手机号',blank=True)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'qy_member'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


# 实体类
class MemberSerializer(ModelSerializer):
    class Meta:
        model = QyMember
        fields = ('id','openid','avatar','age','nickname','phonenum','add_time')



class Member_feedback(ModelSerializer):
    class Meta:
        model = QyMember
        fields = ('id','age','avatar','nickname','phonenum','profession')


class MemberPayment(ModelSerializer):
    class Meta:
        model = QyMember
        exclude = ('openid','unionid','avatar','age','profession','add_time')


class MemberLister(ModelSerializer):
    class Meta:
        model = QyMember
        fields = '__all__'


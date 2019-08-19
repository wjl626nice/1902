"""
招生模块
"""
# coding=utf8
from django.db import models
from account.models import UserRole, NewUser


class Followup_state(models.Model):
    '''
    跟进状态记录
    '''
    # 跟进学生
    f_s_name = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='f_s_name')
    # 跟进描述
    f_info = models.CharField(max_length=200)
    # 跟进时间
    f_date = models.DateField(auto_now_add=True)
    #  录入人
    f_record_person = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='f_record_person')
    # 录入时间
    add_time = models.DateTimeField(auto_now_add=True)


class Source_distribution(models.Model):
    '''
    生源分配表
    '''
    # 学生
    student = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='sd_student')
    # 咨询顾问`
    consultant = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='sd_consultants')

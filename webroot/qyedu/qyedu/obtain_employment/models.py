"""
就业模块
"""
from django.db import models
from account.models import NewUser


class Enterprise(models.Model):
    """
    企业
    """
    e_name = models.CharField(max_length=100)
    e_address = models.CharField(max_length=100)
    e_contact = models.CharField(max_length=10)
    e_contact_phone = models.CharField(max_length=11)
    e_prtocol = models.ImageField(upload_to='e_protocol/%Y%m%d/')
    add_time = models.DateTimeField(auto_now_add=True)


class Suggestion_employment_record(models.Model):
    """
    就业推荐记录
    """
    s_name = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, verbose_name='就业人', related_name='s_name')
    record_person = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, verbose_name='录入人',related_name='record_person')
    e_name = models.CharField(max_length=50)
    e_address = models.CharField(max_length=50)
    stu_feedback = models.CharField(max_length=500)
    emp_result = models.CharField(max_length=10)
    emp_date = models.DateTimeField(auto_now=True)
    add_time = models.DateTimeField(auto_now_add=True)


class VisitedRecord(models.Model):
    """
    回访记录
    """
    v_name = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, verbose_name='回访对象', related_name='v_name')
    visited_date = models.DateField(auto_now=True)
    visited_info = models.CharField(max_length=500)
    v_del_method = models.CharField(max_length=50)
    if_join_talentpool = models.BooleanField(default=0)
    record_person = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='record_persons')
    add_time = models.DateField(auto_now=True)

"""
学习模块
"""
from django.db import models
from account.models import NewUser
from give_lessons.models import LessonsPlan
import time
import datetime

# Create your models here.
class SignIn(models.Model):
    choices = (
        (1, '上午签到'),
        (2, '下午签到'),
        (3, '晚上签到'),
        (4, '晚上放学签到'),
        (5, '迟到/早退')
    )
    sign_in = models.IntegerField(choices=choices)
    date_time = models.DateTimeField(auto_now_add=True)
    my_ip = models.CharField(max_length=30, default='127.0.0.1')
    student_id = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    is_del = models.IntegerField(default=0)

    class Meta:
        db_table = 'sign_in'


class WeekendSummarize(models.Model):
    content = models.CharField(max_length=500)
    student_id = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(blank=True, null=True, auto_now=True)
    score = models.PositiveIntegerField(null=True, blank=True)
    score_date = models.DateTimeField(null=True, blank=True)
    is_del = models.IntegerField(default=0)

    class Meta:
        db_table = 'weekend_summarize'

    def is_expire(self):
        """
        只能修改当周发布内容
        :return:
        """
        return datetime.datetime.now().year == self.publish_date.year \
            and datetime.datetime.now().isocalendar()[1] == self.publish_date.isocalendar()[1]



class Evaluate(models.Model):
    student_id = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    evaluete_content = models.CharField(max_length=200)
    plub_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    give_les = models.ForeignKey(LessonsPlan, on_delete=models.DO_NOTHING)
    is_del = models.IntegerField(default=0)
    knowledges = models.CharField(max_length=500)


    class Meta:
        db_table = 'evaluate'

    def is_expire(self):
        """
        只能修改当周发布的意见反馈
        :return:
        """
        return datetime.datetime.now().year == self.plub_date.year and datetime.datetime.now().month == self.plub_date.month and datetime.datetime.now().day == self.plub_date.day
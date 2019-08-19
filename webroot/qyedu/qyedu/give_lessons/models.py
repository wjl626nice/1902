"""
授课模块
"""
# coding=utf8
from django.db import models
from account.models import NewUser
from new_admin.models import ClassGrade


class LessonsPlan(models.Model):
    les_plan = models.CharField(max_length=500)
    class_grade_id = models.ForeignKey(ClassGrade, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    task_des = models.CharField(max_length=200)
    task_check_date = models.DateTimeField(blank=True, null=True)
    lessons_date = models.DateField()
    add_date = models.DateTimeField(auto_now_add=True)
    is_del = models.IntegerField(default=0)

    class Meta:
        db_table = 'lessons_plan'


class Knowledge(models.Model):
    name = models.CharField(max_length=100)
    grasp_level = models.CharField(max_length=20)
    lessonsplan = models.ForeignKey(LessonsPlan, on_delete=models.CASCADE, related_name='knowledges')
    is_del = models.IntegerField(default=0)
    add_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'knowledge'






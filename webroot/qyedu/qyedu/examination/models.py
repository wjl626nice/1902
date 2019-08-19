"""
考试模块
"""
from django.db import models
from account.models import NewUser
from new_admin.models import ClassGrade


class Exam(models.Model):
    """
    考试表
    """
    user = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='exam')
    class_room = models.ForeignKey(ClassGrade,on_delete=models.DO_NOTHING, related_name='examroom')
    course = models.CharField(max_length=20)
    exam_time = models.DateField()
    score = models.PositiveSmallIntegerField(default=0)
    choice = (
        (0, '周考'),
        (1, '阶段考'),
    )
    category = models.PositiveSmallIntegerField(choices=choice,default=0)
    user_tea = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING,related_name='examtea')
    is_del = models.IntegerField(default=0)

    class Meta:
        db_table = 'Exam'


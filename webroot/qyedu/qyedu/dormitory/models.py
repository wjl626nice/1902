"""
宿舍模块
"""
# coding=utf8
from django.db import models
from account.models import NewUser
from new_admin.models import Dorm


class DorStu(models.Model):
    """
    宿舍学生表，学生分配给哪个宿舍在此表保存
    """
    user = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='dorstu_user_id')
    dormitory = models.ForeignKey(Dorm, on_delete=models.DO_NOTHING, null=True)
    entry_date = models.DateField(null=True)
    leave_date = models.DateField(null=True)
    headmaster = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING, related_name='dorstu_headmaster')
    is_del = models.IntegerField(default=0)


class DormHandle(models.Model):
    """
    宿舍问题处理记录
    """
    dormitory_name = models.ForeignKey(Dorm, on_delete=models.DO_NOTHING)
    user_name = models.CharField(max_length=30)
    dor_problem = models.CharField(max_length=500)
    handle_date = models.DateTimeField(null=True)
    choice = (
        (0, '未解决'),
        (1, '待解决'),
        (2, '已解决'),
    )
    result = models.PositiveSmallIntegerField(choices=choice, default=1)
    add_user = models.ForeignKey(NewUser, on_delete=models.DO_NOTHING)
    add_date = models.DateTimeField(auto_now_add=True)
    is_del = models.IntegerField(default=0)

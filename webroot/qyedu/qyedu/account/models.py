from django.db import models
from django.contrib.auth.models import User


class UserRole(models.Model):
    """
    用户角色表。
    """
    role_name = models.CharField(max_length=20)

    def __str__(self):
        return self.role_name


class NewUser(models.Model):
    """
    用户资料表
    """
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    realname = models.CharField(max_length=15)
    role = models.ForeignKey(UserRole, on_delete=models.DO_NOTHING)
    mobile_number = models.CharField(max_length=15)
    id_card = models.CharField(max_length=25)
    birthday = models.DateField(null=True, blank=True)
    info = models.TextField()
    choice = (
        (0,'女'),
        (1,'男'),
    )
    gender = models.PositiveSmallIntegerField(choices=choice, default=1)
    edu_level = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100)
    choice_s = (
        (0,'未激活'),
        (1,'已激活'),
        (2,'结业'),
        (3,'退学')
    )
    state = models.PositiveSmallIntegerField(choices=choice_s, default=0)
    choice_is = (
        (0,'否'),
        (1,'是'),
    )
    is_goodman = models.PositiveSmallIntegerField(choices=choice_is, default=0)
    choice_del = (
        (0,'正常'),
        (1,'删除'),
    )
    is_del = models.PositiveSmallIntegerField(choices=choice_del, default=0)
    choice_pay = (
        (0, '未设定'),
        (1, '贷款缴费'),
        (2, '现金缴费')
    )
    pay_mode = models.PositiveSmallIntegerField(choices=choice_pay, default=0)

    def __str__(self):
        return self.realname

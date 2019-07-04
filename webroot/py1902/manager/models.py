from django.db import models

# Create your models here.

class Admin(models.Model):
    account = models.CharField(max_length=30, unique=True, verbose_name='账号', default='')
    email = models.CharField(max_length=45, unique=True, verbose_name='邮箱', default='')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号', default='')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    login_num = models.PositiveIntegerField(verbose_name='登录次数', default=0)
    login_time = models.DateTimeField(auto_now=True, verbose_name='最后一次登录时间')
    login_ip = models.CharField(max_length=15, verbose_name='ipv4地址')
    state = models.BooleanField(default=False, verbose_name="状态，1禁用 0正常")

    class Meta:
        # db_table = 'pyadmin',   # 自定义表名 解决
        ordering = '-id',
        verbose_name = '管理员表'
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


# 自定义字段 tinyint
class CustomeTinyIntField(models.Field):
    def __init__(self,max_length,*args,**kwargs):
        self.max_length = max_length
        super(CustomeTinyIntField,self).__init__(max_length=max_length,*args,**kwargs)

    def db_type(self,connection):
        return 'tinyint(%s)'%self.max_length

# 自定义字段 TimeStamp
class CustomeTimeStampField(models.Field):
    def __init__(self, *args, **kwargs):
        super(CustomeTimeStampField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'timestamp default CURRENT_TIMESTAMP'

# 管理员模型
class Admin(models.Model):
    account = models.CharField(max_length=30, unique=True, verbose_name='账号', default='')
    nickname = models.CharField(max_length=45, default='', verbose_name='昵称')
    email = models.CharField(max_length=45, unique=True, verbose_name='邮箱', default='')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号', default='')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    login_num = models.PositiveIntegerField(verbose_name='登录次数', default=0)
    login_time = models.DateTimeField(default=timezone.now, verbose_name='最后一次登录时间')
    login_ip = models.CharField(max_length=15, verbose_name='ipv4地址')
    state = models.BooleanField(default=True, verbose_name="状态，1禁用 0正常")
    access_token = models.CharField(max_length=32,unique=True, verbose_name='令牌')

    class Meta:
        # db_table = 'pyadmin',   # 自定义表名 解决
        ordering = '-id',
        verbose_name = '管理员表'


# 管理员操作日志模型
class Admin_log(models.Model):
    type = models.CharField(max_length=10, verbose_name='操作类型')
    title = models.CharField(max_length=150, verbose_name='操作日志标题')
    add_time = models.DateTimeField(default=timezone.now, verbose_name='操作时间')
    user_agent = models.CharField(max_length=240, verbose_name='记录用户客户端信息')
    referer = models.CharField(max_length=100, verbose_name='操作来源页')
    ip = models.CharField(max_length=15, verbose_name='ip')
    admin = models.ForeignKey(to=Admin, verbose_name='管理员模型的外键', on_delete=models.DO_NOTHING)

    class META:
        table_name = 'p1_admin_log'
        ordering = '-id',
        verbose_name = '管理员日志表'
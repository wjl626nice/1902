from django.db import models
from django.utils import timezone
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
    email = models.CharField(max_length=45, unique=True, verbose_name='邮箱', default='')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号', default='')
    pwd = models.CharField(max_length=32, verbose_name='密码')
    login_num = models.PositiveIntegerField(verbose_name='登录次数', default=0)
    login_time = models.DateTimeField(default=timezone.now, verbose_name='最后一次登录时间')
    login_ip = models.CharField(max_length=15, verbose_name='ipv4地址')
    state = models.BooleanField(default=True, verbose_name="状态，1禁用 0正常")

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


# 栏目管理模型
class Category(models.Model):
    cate_name = models.CharField(max_length=25, default='', verbose_name='栏目名称')
    describles = models.CharField(max_length=200, default='', verbose_name='栏目描述')
    pic = models.ImageField(max_length=150, upload_to='static/upload/%Y%m%d/', default='', verbose_name='栏目图片')
    seo_title = models.CharField(max_length=50, verbose_name='seo标题')
    seo_keyword = models.CharField(max_length=60, verbose_name='seo关键词')
    seo_description = models.CharField(max_length=200, verbose_name='seo描述')
    num = models.PositiveIntegerField(default=0, verbose_name='发布文章数')


# 文章管理模型
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='标题')
    category = models.ForeignKey(to="Category", on_delete=models.DO_NOTHING, verbose_name='栏目id')
    tags = models.CharField(max_length=50, default='', verbose_name='标签')
    describles = models.CharField(max_length=200, verbose_name='描述')
    pic = models.ImageField(upload_to='static/upload/article/%Y%m%d/', verbose_name='图片')
    flag = CustomeTinyIntField(max_length=1, default=0, verbose_name='文章推荐 0默认 1置顶 2 推荐')
    add_time = CustomeTimeStampField(verbose_name='添加时间')
    admin = models.ForeignKey(to='Admin', on_delete=models.DO_NOTHING, verbose_name='添加人')
    click = models.PositiveIntegerField(verbose_name='点击量', default=0)
    support = models.PositiveIntegerField(verbose_name='点赞', default=0)
    seo_title = models.CharField(max_length=50, verbose_name='seo标题')
    seo_keyword = models.CharField(max_length=60, verbose_name='seo关键词')
    seo_description = models.CharField(max_length=200, verbose_name='seo描述')


# 文章管理模型
class Atricle_additional(models.Model):
    article = models.OneToOneField(to='Article', primary_key=True, default=0, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='文章内容')














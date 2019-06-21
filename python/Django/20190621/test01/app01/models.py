from django.db import models
from django.utils import timezone

# Create your models here.
# 栏目模型
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    cate_name = models.CharField(max_length=35, null=False, unique=True)
    describles = models.CharField(max_length=150,null=True)
# 文章模型
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    # 跟栏目关联字段
    category = models.ForeignKey(to='Category', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=120, default='')
    # 设置当前默认时间
    add_time = models.DateTimeField(default=timezone.now)
    # 预览量
    click = models.IntegerField(default=0)
    # 正文
    content = models.TextField()

# 出版社
class Presssss(models.Model):
    name = models.CharField(max_length=35, unique=True)
    # zid = models.AutoField(primary_key=True)
    # 模型元数据
    class Meta:
        db_table = 'p_press'  #自定义表名

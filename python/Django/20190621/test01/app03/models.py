from django.db import models
from django.utils import timezone
# Create your models here.
# 文章基础模型
class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120, default='')
    # 设置当前默认时间
    add_time = models.DateTimeField(default=timezone.now)
    # 预览量
    click = models.IntegerField(default=0)

    class Meta:
        pass
        # 联合普通索引
        # index_together = ('title', 'add_time')
        # 联合唯一索引
        # unique_together = ('title', 'add_time')
# 文章附加模型
class Articles_Content(models.Model):
    # 一对一关系
    article = models.OneToOneField(Articles, primary_key=True, on_delete=models.CASCADE, related_name='ac')
    # 正文
    content = models.TextField()
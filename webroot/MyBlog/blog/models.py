from django.db import models

# Create your models here.
# 栏目管理模型
class Category(models.Model):
    cate_name = models.CharField(max_length=25, default='', verbose_name='栏目名称')
    describles = models.CharField(max_length=200, default='', verbose_name='栏目描述')
    pic = models.ImageField(max_length=150, upload_to='static/upload/%Y%m%d/', default='', verbose_name='栏目图片')
    is_menu = models.BooleanField(default=True, verbose_name='是否在首页栏目中展示')
    weight = models.PositiveSmallIntegerField(default=0, verbose_name='控制栏目排序')
    seo_title = models.CharField(max_length=50, verbose_name='seo标题')
    seo_keyword = models.CharField(max_length=60, verbose_name='seo关键词')
    seo_description = models.CharField(max_length=200, verbose_name='seo描述')
    num = models.PositiveIntegerField(default=0, verbose_name='发布文章数')

    def __str__(self):
        return self.cate_name

    class Meta:
        ordering = '-id',
        verbose_name = '栏目管理'
        verbose_name_plural = '栏目管理'
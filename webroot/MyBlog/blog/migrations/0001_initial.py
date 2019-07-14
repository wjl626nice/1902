# Generated by Django 2.2 on 2019-07-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(default='', max_length=25, verbose_name='栏目名称')),
                ('describles', models.CharField(default='', max_length=200, verbose_name='栏目描述')),
                ('pic', models.ImageField(default='', max_length=150, upload_to='static/upload/%Y%m%d/', verbose_name='栏目图片')),
                ('is_menu', models.BooleanField(default=True, verbose_name='是否在首页栏目中展示')),
                ('weight', models.PositiveSmallIntegerField(default=0, verbose_name='控制栏目排序')),
                ('seo_title', models.CharField(max_length=50, verbose_name='seo标题')),
                ('seo_keyword', models.CharField(max_length=60, verbose_name='seo关键词')),
                ('seo_description', models.CharField(max_length=200, verbose_name='seo描述')),
                ('num', models.PositiveIntegerField(default=0, verbose_name='发布文章数')),
            ],
            options={
                'verbose_name': '栏目管理',
                'verbose_name_plural': '栏目管理',
                'ordering': ('-id',),
            },
        ),
    ]

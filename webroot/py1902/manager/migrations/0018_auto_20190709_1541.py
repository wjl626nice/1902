# Generated by Django 2.2 on 2019-07-09 15:41

from django.db import migrations, models
import manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_auto_20190709_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_menu',
            field=models.BooleanField(default=True, verbose_name='是否在首页栏目中展示'),
        ),
        migrations.AddField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='控制栏目排序'),
        ),
        migrations.AlterField(
            model_name='article',
            name='add_time',
            field=manager.models.CustomeTimeStampField(default='2019-07-09 15:41:06', verbose_name='添加时间'),
        ),
    ]
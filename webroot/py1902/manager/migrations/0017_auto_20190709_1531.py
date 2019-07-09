# Generated by Django 2.2 on 2019-07-09 15:31

from django.db import migrations
import manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_auto_20190709_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_menu',
        ),
        migrations.AlterField(
            model_name='article',
            name='add_time',
            field=manager.models.CustomeTimeStampField(default='2019-07-09 15:31:50', verbose_name='添加时间'),
        ),
    ]

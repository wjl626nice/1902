# Generated by Django 2.2 on 2019-06-20 06:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190620_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

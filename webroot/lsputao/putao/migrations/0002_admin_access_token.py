# Generated by Django 2.2 on 2019-07-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('putao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='access_token',
            field=models.CharField(default='', max_length=32, unique=True, verbose_name='令牌'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2 on 2019-06-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_auto_20190621_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='sales_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

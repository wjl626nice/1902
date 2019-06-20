# Generated by Django 2.2 on 2019-06-20 06:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='describles',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=120)),
                ('add_time', models.DateTimeField(default=datetime.datetime(2019, 6, 20, 6, 23, 11, 168717, tzinfo=utc))),
                ('click', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Category')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-05-31 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=35, unique=True)),
            ],
        ),
    ]

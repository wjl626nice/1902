# Generated by Django 2.2 on 2019-07-05 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20190705_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='account',
            new_name='accounts',
        ),
    ]

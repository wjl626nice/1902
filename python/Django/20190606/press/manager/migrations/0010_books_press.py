# Generated by Django 2.2 on 2019-06-04 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='press',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.Press'),
        ),
    ]

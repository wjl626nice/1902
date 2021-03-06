# Generated by Django 2.2 on 2019-06-25 02:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=120)),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('click', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Articles_Content',
            fields=[
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ac', serialize=False, to='app02.Articles')),
                ('content', models.TextField()),
            ],
        ),
    ]

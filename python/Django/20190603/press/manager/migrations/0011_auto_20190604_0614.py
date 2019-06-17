# Generated by Django 2.2 on 2019-06-04 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_books_press'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='press',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.Press'),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('bookss', models.ManyToManyField(to='manager.Books')),
            ],
        ),
    ]
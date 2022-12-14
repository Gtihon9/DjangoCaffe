# Generated by Django 4.0.7 on 2022-10-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caffe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='main_photo')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
    ]

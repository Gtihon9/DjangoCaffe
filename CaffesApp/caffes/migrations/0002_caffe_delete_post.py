# Generated by Django 4.0.7 on 2022-10-03 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caffes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caffe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('rating', models.FloatField(max_length=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

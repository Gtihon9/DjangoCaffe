# Generated by Django 4.0.7 on 2022-10-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caffes', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_id',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2 on 2021-05-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0003_auto_20210508_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='prints',
            name='icon',
            field=models.IntegerField(default=0),
        ),
    ]

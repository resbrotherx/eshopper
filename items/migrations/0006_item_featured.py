# Generated by Django 3.1.3 on 2021-04-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20210404_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='featured',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]

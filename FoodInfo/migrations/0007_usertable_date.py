# Generated by Django 3.0.8 on 2020-08-18 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodInfo', '0006_auto_20200818_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='날짜'),
        ),
    ]

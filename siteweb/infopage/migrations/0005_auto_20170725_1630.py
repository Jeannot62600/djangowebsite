# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infopage', '0004_auto_20170725_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='slug',
            field=models.CharField(default='8JqsMU', max_length=6, unique=True),
        ),
    ]

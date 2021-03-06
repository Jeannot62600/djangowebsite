# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 12:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Projet', 'verbose_name_plural': 'Projets'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Catégorie', 'verbose_name_plural': 'Catégories'},
        ),
        migrations.AddField(
            model_name='project',
            name='difficulty',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='project',
            name='fiche',
            field=models.TextField(default='No Fiche Yet'),
        ),
        migrations.AddField(
            model_name='project',
            name='fini',
            field=models.BooleanField(default=True),
        ),
    ]

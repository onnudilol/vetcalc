# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rxcalc', '0010_medication_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='slug',
            field=models.SlugField(default='', max_length=40, unique=True),
        ),
    ]

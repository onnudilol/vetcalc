# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rxcalc', '0004_medication_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='desc',
            field=models.TextField(blank=True, default=''),
        ),
    ]
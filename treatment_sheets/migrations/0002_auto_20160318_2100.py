# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 21:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_prescription'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treatment_sheets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='txitem',
            name='dose',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='txitem',
            name='freq',
            field=models.CharField(choices=[('SID', 'SID'), ('BID', 'BID')], default='', max_length=5),
        ),
        migrations.AddField(
            model_name='txitem',
            name='instruction',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='txitem',
            name='med',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='common.Prescription'),
        ),
        migrations.AddField(
            model_name='txitem',
            name='sheet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='treatment_sheets.TxSheet'),
        ),
        migrations.AddField(
            model_name='txitem',
            name='unit',
            field=models.CharField(choices=[('mL', 'mLs'), ('C', 'Capsules'), ('T', 'Tablets')], default='', max_length=5),
        ),
        migrations.AddField(
            model_name='txsheet',
            name='comment',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='txsheet',
            name='name',
            field=models.CharField(default='', max_length=140),
        ),
        migrations.AddField(
            model_name='txsheet',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

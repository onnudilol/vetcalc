# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=140, unique=True)),
                ('slug', models.SlugField(default='', max_length=40, unique=True)),
                ('category', models.CharField(blank=True, default='', max_length=140)),
                ('concentration', models.CharField(blank=True, default='', max_length=140)),
                ('desc', models.TextField(blank=True, default='')),
                ('calc_type', models.CharField(choices=[('ez', 'Simple'), ('adv', 'Advanced')], default='', max_length=3)),
                ('rates', jsonfield.fields.JSONField()),
                ('units', models.CharField(default='', max_length=3)),
            ],
            options={
                'abstract': False,
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Injection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=140, unique=True)),
                ('slug', models.SlugField(default='', max_length=40, unique=True)),
                ('category', models.CharField(blank=True, default='', max_length=140)),
                ('concentration', models.CharField(blank=True, default='', max_length=140)),
                ('desc', models.TextField(blank=True, default='')),
                ('factor', models.FloatField(default=0.0)),
                ('admin', models.CharField(blank=True, default='', max_length=140)),
            ],
            options={
                'abstract': False,
                'ordering': ['category', 'name'],
            },
        ),
    ]
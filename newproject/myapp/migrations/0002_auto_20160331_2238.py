# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='difficulty',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.CharField(max_length=20),
        ),
    ]
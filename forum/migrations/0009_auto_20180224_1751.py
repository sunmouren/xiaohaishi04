# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-02-24 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20180224_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(blank=True, max_length=128, verbose_name='概要，若留空，则自动使用内容前30个字符'),
        ),
    ]

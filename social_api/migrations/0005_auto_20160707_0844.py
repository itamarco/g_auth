# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_api', '0004_auto_20160706_2252'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ApiResponse',
        ),
        migrations.DeleteModel(
            name='GoogleUserInfo',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-13 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20171013_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='test',
            field=models.CharField(db_column='测试', max_length=32, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailers', '0002_sendmails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendmails',
            name='process_finish_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 16, 13, 15, 120193), editable=False),
        ),
        migrations.AlterField(
            model_name='sendmails',
            name='process_start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 16, 13, 15, 120154), editable=False),
        ),
    ]

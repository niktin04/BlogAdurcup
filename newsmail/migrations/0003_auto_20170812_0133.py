# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsmail', '0002_newsmail_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmail',
            name='img_url',
            field=models.CharField(default='#', max_length=1000),
        ),
    ]

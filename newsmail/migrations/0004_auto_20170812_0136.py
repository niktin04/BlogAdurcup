# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsmail', '0003_auto_20170812_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmail',
            name='author',
            field=models.CharField(default='Adurcup', max_length=100),
        ),
    ]

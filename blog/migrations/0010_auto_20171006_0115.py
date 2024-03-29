# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]

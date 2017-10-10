# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_start_time', models.DateTimeField(default=datetime.datetime(2017, 10, 10, 16, 13, 10, 426024), editable=False)),
                ('process_finish_time', models.DateTimeField(default=datetime.datetime(2017, 10, 10, 16, 13, 10, 426063), editable=False)),
                ('exceptions', models.IntegerField(default=0, editable=False)),
                ('mails_sent', models.IntegerField(default=0, editable=False)),
                ('mailer_to_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailers.Mailers')),
            ],
        ),
    ]

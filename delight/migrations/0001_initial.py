# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 12:55
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('content', ckeditor.fields.RichTextField()),
                ('img_url', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='DelightTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delight.Delight')),
            ],
        ),
    ]

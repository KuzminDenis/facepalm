# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 23:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fp_app', '0004_palmer_processed_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palmer',
            name='processed_image',
        ),
    ]

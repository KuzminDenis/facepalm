# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='palmer',
            name='processed_image',
            field=models.ImageField(blank=True, upload_to='photos/processed'),
        ),
    ]

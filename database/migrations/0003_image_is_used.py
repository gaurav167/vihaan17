# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_storage__hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_used',
            field=models.BooleanField(default=0),
        ),
    ]

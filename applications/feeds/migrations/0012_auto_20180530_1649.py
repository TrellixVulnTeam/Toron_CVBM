# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-30 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0011_auto_20180530_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.AskaQuestion'),
        ),
    ]

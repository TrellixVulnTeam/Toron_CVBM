# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-12 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0062_auto_20180810_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsweraQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000)),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeds.AskaQuestion')),
            ],
        ),
    ]

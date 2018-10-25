# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-25 13:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0045_comments_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='like',
        ),
        migrations.AddField(
            model_name='comments',
            name='likes_comment',
            field=models.ManyToManyField(blank=True, related_name='likes_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 2.0.7 on 2018-07-21 03:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0033_auto_20180720_2005'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hidden',
            unique_together={('user', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=set(),
        ),
    ]
# Generated by Django 2.0.7 on 2018-07-21 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0036_auto_20180720_2016'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='tags',
            unique_together=set(),
        ),
    ]

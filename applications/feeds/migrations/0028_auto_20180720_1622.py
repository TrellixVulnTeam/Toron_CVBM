# Generated by Django 2.0.7 on 2018-07-20 23:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0027_auto_20180720_1620'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tags',
            unique_together={('user', 'my_tag', 'my_subtag')},
        ),
    ]

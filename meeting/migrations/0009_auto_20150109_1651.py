# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0008_auto_20150109_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='participants',
            field=models.ManyToManyField(to='meeting.Member', blank=True),
            preserve_default=True,
        ),
    ]

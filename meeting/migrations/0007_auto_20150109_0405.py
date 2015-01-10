# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0006_auto_20150109_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingitem',
            name='presenter',
            field=models.ForeignKey(to='meeting.Member', null=True),
            preserve_default=True,
        ),
    ]

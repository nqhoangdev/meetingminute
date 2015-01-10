# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0004_auto_20150109_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='meetingitem',
            name='meeting',
        ),
        migrations.DeleteModel(
            name='Meeting',
        ),
        migrations.RemoveField(
            model_name='meetingitem',
            name='presenter',
        ),
        migrations.DeleteModel(
            name='MeetingItem',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]

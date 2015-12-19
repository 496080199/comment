# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0025_auto_20151209_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 17, 27, 47, 907000), auto_now=True),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='time',
            field=models.DateTimeField(default=None, auto_now=True),
            preserve_default=False,
        ),
    ]

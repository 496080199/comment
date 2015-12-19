# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_work_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='count',
        ),
        migrations.AddField(
            model_name='applicate',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]

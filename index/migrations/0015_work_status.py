# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20151207_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0027_auto_20151210_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=3),
        ),
    ]

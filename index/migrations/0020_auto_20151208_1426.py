# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_auto_20151208_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicate',
            name='content',
        ),
        migrations.AddField(
            model_name='applicate',
            name='time',
            field=models.DateTimeField(default=None, auto_now=True),
            preserve_default=False,
        ),
    ]

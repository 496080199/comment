# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0026_auto_20151209_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='work',
        ),
        migrations.AddField(
            model_name='comment',
            name='applicate',
            field=models.OneToOneField(default=None, to='index.Applicate'),
            preserve_default=False,
        ),
    ]

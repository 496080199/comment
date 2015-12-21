# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20151221_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='auth_result',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]

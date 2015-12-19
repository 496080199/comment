# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_work_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]

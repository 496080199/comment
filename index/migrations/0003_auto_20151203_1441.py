# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_applicate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

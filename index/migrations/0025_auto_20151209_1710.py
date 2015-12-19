# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0024_auto_20151209_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='teacher',
            field=models.ForeignKey(to='index.Teacher'),
        ),
    ]

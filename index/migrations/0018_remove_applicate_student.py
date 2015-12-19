# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_work_addit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicate',
            name='student',
        ),
    ]

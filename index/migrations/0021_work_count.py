# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0020_auto_20151208_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]

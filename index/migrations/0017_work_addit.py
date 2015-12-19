# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20151208_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='addit',
            field=models.TextField(null=True),
        ),
    ]

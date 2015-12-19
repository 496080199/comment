# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_remove_applicate_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicate',
            name='ispass',
        ),
        migrations.AddField(
            model_name='applicate',
            name='stat',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

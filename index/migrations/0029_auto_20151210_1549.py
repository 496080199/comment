# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0028_comment_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evluate',
            name='student',
        ),
        migrations.RemoveField(
            model_name='evluate',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Evluate',
        ),
    ]

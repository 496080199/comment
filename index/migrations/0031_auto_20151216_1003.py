# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0030_auto_20151216_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='file',
            new_name='video',
        ),
        migrations.AddField(
            model_name='comment',
            name='audio',
            field=models.FileField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/comment/%Y/%m/%d', blank=True),
        ),
    ]

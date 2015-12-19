# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20151207_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='file',
            field=models.FileField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/work/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/workimg/%Y/%m/%d', blank=True),
        ),
    ]

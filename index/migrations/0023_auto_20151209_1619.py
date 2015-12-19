# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_auto_20151209_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicate',
            name='show',
        ),
        migrations.AddField(
            model_name='comment',
            name='file',
            field=models.FileField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/comment/%Y/%m/%d', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/comment/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/work/%Y/%m/%d', blank=True),
        ),
    ]

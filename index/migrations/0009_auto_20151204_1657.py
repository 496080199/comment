# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20151204_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='height',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AddField(
            model_name='teacher',
            name='width',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(default=b'D:/eclipse/workplace/comment/media/touxiang.jpg', height_field=b'height', width_field=b'width', upload_to=b'D:/eclipse/workplace/comment/media/teacher/%Y/%m/%d/%H/%i/%s'),
        ),
    ]

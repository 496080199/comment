# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0029_auto_20151210_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='file',
            new_name='video',
        ),
        migrations.AddField(
            model_name='work',
            name='audio',
            field=models.FileField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/work/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(default=b'D:/eclipse/workplace/comment/media/touxiang.jpg', upload_to=b'D:/eclipse/workplace/comment/media/img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(default=b'D:/eclipse/workplace/comment/media/touxiang.jpg', upload_to=b'D:/eclipse/workplace/comment/media/img/%Y/%m/%d'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20151204_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(default=b'D:/eclipse/workplace/comment/media/touxiang.jpg', height_field=b'30', width_field=b'30', upload_to=b'D:/eclipse/workplace/comment/media/student/%Y/%m/%d/%H/%i/%s'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(default=b'D:/eclipse/workplace/comment/media/touxiang.jpg', height_field=b'30', width_field=b'30', upload_to=b'D:/eclipse/workplace/comment/media/teacher/%Y/%m/%d/%H/%i/%s'),
        ),
    ]

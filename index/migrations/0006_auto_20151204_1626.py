# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20151204_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/student/%Y/%m/%d/%H/%i/%s'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='img',
            field=models.ImageField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/teacher/%Y/%m/%d/%H/%i/%s'),
        ),
        migrations.AlterField(
            model_name='work',
            name='file',
            field=models.FileField(upload_to=b'D:/eclipse/workplace/comment/media/work/%Y/%m/%d/%H/%i/%s'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/workimg/%Y/%m/%d/%H/%i/%s'),
        ),
    ]

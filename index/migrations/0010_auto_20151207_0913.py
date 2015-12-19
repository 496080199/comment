# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20151204_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='height',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='width',
        ),
        migrations.AddField(
            model_name='student',
            name='area',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='province',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='area',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='city',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='province',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='desc',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='time',
            field=models.DateTimeField(default=None, auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(default=b'/media//touxiang.jpg', upload_to=b'D:/eclipse/workplace/comment/media/student/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(default=b'/media//touxiang.jpg', upload_to=b'D:/eclipse/workplace/comment/media/teacher/%Y/%m/%d/%H/%i/%s'),
        ),
        migrations.AlterField(
            model_name='work',
            name='file',
            field=models.FileField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/work/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/workimg/%Y/%m/%d'),
        ),
    ]

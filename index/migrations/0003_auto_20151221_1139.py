# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20151221_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='audio',
            field=models.FileField(null=True, upload_to=b'comment/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(null=True, upload_to=b'comment/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.FileField(null=True, upload_to=b'comment/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default=b'touxiang.jpg', upload_to=b'img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='othercert',
            field=models.ImageField(null=True, upload_to=b'cert/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='workshow',
            field=models.FileField(null=True, upload_to=b'cert/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='audio',
            field=models.FileField(null=True, upload_to=b'work/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(null=True, upload_to=b'work/%Y/%m/%d', blank=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='video',
            field=models.FileField(null=True, upload_to=b'work/%Y/%m/%d', blank=True),
        ),
    ]

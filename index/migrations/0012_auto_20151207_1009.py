# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20151207_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(default=b'D:/eclipse/workplace/comment/media/touxiang.jpg', upload_to=b'D:/eclipse/workplace/comment/media/teacher/%Y/%m/%d'),
        ),
    ]

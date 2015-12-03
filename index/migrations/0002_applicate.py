# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('ispass', models.BooleanField()),
                ('student', models.ForeignKey(to='index.Student')),
                ('teacher', models.ForeignKey(to='index.Teacher')),
                ('work', models.ForeignKey(to='index.Work')),
            ],
        ),
    ]

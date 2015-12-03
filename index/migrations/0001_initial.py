# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Evluate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sex', models.CharField(max_length=100)),
                ('birth', models.DateTimeField()),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=11)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sex', models.CharField(max_length=100)),
                ('birth', models.DateTimeField()),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=11)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=b'D:/eclipse/workplace/comment/media/work/%Y/%m/%d')),
                ('image', models.ImageField(null=True, upload_to=b'D:/eclipse/workplace/comment/media/workimg/%Y/%m/%d')),
                ('student', models.ForeignKey(to='index.Student')),
            ],
        ),
        migrations.AddField(
            model_name='evluate',
            name='student',
            field=models.ForeignKey(to='index.Student'),
        ),
        migrations.AddField(
            model_name='evluate',
            name='teacher',
            field=models.OneToOneField(to='index.Teacher'),
        ),
        migrations.AddField(
            model_name='comment',
            name='teacher',
            field=models.OneToOneField(to='index.Teacher'),
        ),
        migrations.AddField(
            model_name='comment',
            name='work',
            field=models.ForeignKey(to='index.Work'),
        ),
    ]

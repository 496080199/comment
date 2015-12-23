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
            name='Applicate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('stat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('video', models.FileField(null=True, upload_to=b'comment/%Y/%m/%d', blank=True)),
                ('audio', models.FileField(null=True, upload_to=b'comment/%Y/%m/%d', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'comment/%Y/%m/%d', blank=True)),
                ('status', models.IntegerField(default=1)),
                ('score', models.IntegerField(default=2)),
                ('time', models.DateTimeField(auto_now=True)),
                ('applicate', models.OneToOneField(to='index.Applicate')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('obj', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField()),
                ('sex', models.CharField(max_length=100)),
                ('birth', models.DateField()),
                ('province', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('img', models.ImageField(default=b'touxiang.jpg', upload_to=b'img/%Y/%m/%d')),
                ('score', models.IntegerField(default=0)),
                ('auth', models.IntegerField(default=0)),
                ('auth_result', models.CharField(max_length=200)),
                ('cert', models.ImageField(null=True, upload_to=b'cert/%Y/%m/%d')),
                ('othercert', models.ImageField(null=True, upload_to=b'cert/%Y/%m/%d', blank=True)),
                ('workshow', models.FileField(null=True, upload_to=b'cert/%Y/%m/%d', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('video', models.FileField(null=True, upload_to=b'work/%Y/%m/%d', blank=True)),
                ('audio', models.FileField(null=True, upload_to=b'work/%Y/%m/%d', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'work/%Y/%m/%d', blank=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=1)),
                ('addit', models.TextField(null=True)),
                ('student', models.ForeignKey(to='index.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='worktype',
            field=models.ForeignKey(to='index.WorkType'),
        ),
        migrations.AddField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(to='index.Profile'),
        ),
        migrations.AddField(
            model_name='log',
            name='profile',
            field=models.ForeignKey(to='index.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='teacher',
            field=models.ForeignKey(to='index.Profile'),
        ),
        migrations.AddField(
            model_name='applicate',
            name='teacher',
            field=models.ForeignKey(to='index.Profile'),
        ),
        migrations.AddField(
            model_name='applicate',
            name='work',
            field=models.ForeignKey(to='index.Work'),
        ),
    ]

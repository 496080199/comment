from django.db import models
from comment.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.auth.models import User
import os
# Create your models here.
class Teacher(models.Model):
    sex=models.CharField(max_length=100)
    birth=models.DateField()
    province=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    img=models.ImageField(upload_to=MEDIA_ROOT+'/teacher/%Y/%m/%d',default=MEDIA_ROOT+'/touxiang.jpg')
    score=models.IntegerField(default=0)
    user=models.OneToOneField(User)
class Student(models.Model):
    sex=models.CharField(max_length=100)
    birth=models.DateField()
    province=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    img=models.ImageField(upload_to=MEDIA_ROOT+'/student/%Y/%m/%d',default=MEDIA_ROOT+'/touxiang.jpg')
    score=models.IntegerField(default=0)
    user=models.OneToOneField(User)
class Work(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    content=models.TextField()
    file=models.FileField(upload_to=MEDIA_ROOT+'/work/%Y/%m/%d',null=True,blank=True)
    image=models.ImageField(upload_to=MEDIA_ROOT+'/work/%Y/%m/%d',null=True,blank=True)
    time=models.DateTimeField(auto_now=True)
    status=models.IntegerField(default=1)
    addit=models.TextField(null=True)
    student=models.ForeignKey(Student)
    def getfilesuffix(self):
        file_name_suffix=os.path.splitext(self.file.name)[1].lower()
        return file_name_suffix
class Applicate(models.Model):
    teacher=models.ForeignKey(Teacher)
    time=models.DateTimeField(auto_now=True)
    stat=models.IntegerField()
    work=models.ForeignKey(Work)
class Comment(models.Model):
    content=models.TextField()
    file=models.FileField(upload_to=MEDIA_ROOT+'/comment/%Y/%m/%d',null=True,blank=True)
    image=models.ImageField(upload_to=MEDIA_ROOT+'/comment/%Y/%m/%d',null=True,blank=True)
    status=models.IntegerField(default=1)
    score=models.IntegerField(default=3)
    time=models.DateTimeField(auto_now=True)
    applicate=models.OneToOneField(Applicate)



    
    
    
    
    
        
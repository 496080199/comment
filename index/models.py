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
    user=models.OneToOneField(User)
class Work(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    content=models.TextField()
    file=models.FileField(upload_to=MEDIA_ROOT+'/work/%Y/%m/%d',null=True,blank=True)
    image=models.ImageField(upload_to=MEDIA_ROOT+'/workimg/%Y/%m/%d',null=True,blank=True)
    time=models.DateTimeField(auto_now=True)
    student=models.ForeignKey(Student)
    def getfilesuffix(self):
        file_name_suffix=os.path.splitext(self.file.name)[1].lower()
        return file_name_suffix
class Comment(models.Model):
    content=models.CharField(max_length=500)
    work=models.ForeignKey(Work)
    teacher=models.OneToOneField(Teacher)
class Evluate(models.Model):
    content=models.CharField(max_length=500)
    student=models.ForeignKey(Student)
    teacher=models.OneToOneField(Teacher)
class Applicate(models.Model):
    teacher=models.ForeignKey(Teacher)
    content=models.CharField(max_length=500)
    ispass=models.BooleanField()
    work=models.ForeignKey(Work)
    student=models.ForeignKey(Student)
    
    
    
    
    
        
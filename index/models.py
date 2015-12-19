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
    img=models.ImageField(upload_to=MEDIA_ROOT+'/img/%Y/%m/%d',default=MEDIA_ROOT+'/touxiang.jpg')
    score=models.IntegerField(default=0)
    auth=models.IntegerField(default=0)
    cert=models.ImageField(null=True,upload_to=MEDIA_ROOT+'/cert/%Y/%m/%d')
    othercert=models.ImageField(null=True,blank=True,upload_to=MEDIA_ROOT+'/cert/%Y/%m/%d')
    work=models.FileField(upload_to=MEDIA_ROOT+'/cert/%Y/%m/%d',null=True,blank=True)
    user=models.OneToOneField(User)
    def getworksuffix(self):
        file_name_suffix=os.path.splitext(self.work.name)[1].lower()
        return file_name_suffix
class Student(models.Model):
    sex=models.CharField(max_length=100)
    birth=models.DateField()
    province=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    img=models.ImageField(upload_to=MEDIA_ROOT+'/img/%Y/%m/%d',default=MEDIA_ROOT+'/touxiang.jpg')
    score=models.IntegerField(default=0)
    user=models.OneToOneField(User)
class Work(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    content=models.TextField()
    video=models.FileField(upload_to=MEDIA_ROOT+'/work/%Y/%m/%d',null=True,blank=True)
    audio=models.FileField(upload_to=MEDIA_ROOT+'/work/%Y/%m/%d',null=True,blank=True)
    image=models.ImageField(upload_to=MEDIA_ROOT+'/work/%Y/%m/%d',null=True,blank=True)
    time=models.DateTimeField(auto_now=True)
    status=models.IntegerField(default=1)
    addit=models.TextField(null=True)
    student=models.ForeignKey(Student)
    def getvideosuffix(self):
        file_name_suffix=os.path.splitext(self.video.name)[1].lower()
        return file_name_suffix
    def getaudiosuffix(self):
        file_name_suffix=os.path.splitext(self.audio.name)[1].lower()
        return file_name_suffix
class Applicate(models.Model):
    teacher=models.ForeignKey(Teacher)
    time=models.DateTimeField(auto_now=True)
    stat=models.IntegerField()
    work=models.ForeignKey(Work)
class Comment(models.Model):
    content=models.TextField()
    video=models.FileField(upload_to=MEDIA_ROOT+'/comment/%Y/%m/%d',null=True,blank=True)
    audio=models.FileField(upload_to=MEDIA_ROOT+'/comment/%Y/%m/%d',null=True,blank=True)
    image=models.ImageField(upload_to=MEDIA_ROOT+'/comment/%Y/%m/%d',null=True,blank=True)
    status=models.IntegerField(default=1)
    score=models.IntegerField(default=2)
    time=models.DateTimeField(auto_now=True)
    applicate=models.OneToOneField(Applicate)
    def getvideosuffix(self):
        file_name_suffix=os.path.splitext(self.video.name)[1].lower()
        return file_name_suffix
    def getaudiosuffix(self):
        file_name_suffix=os.path.splitext(self.audio.name)[1].lower()
        return file_name_suffix



    
    
    
    
    
        
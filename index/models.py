from django.db import models
from comment.settings import MEDIA_ROOT
from django.contrib.auth.models import User
# Create your models here.
class Teacher(models.Model):
    sex=models.CharField(max_length=100)
    birth=models.DateField()
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    user=models.OneToOneField(User)
class Student(models.Model):
    sex=models.CharField(max_length=100)
    birth=models.DateField()
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    user=models.OneToOneField(User)
class Work(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to=MEDIA_ROOT+'/work/%Y/%m/%d')
    image=models.ImageField(upload_to=MEDIA_ROOT+'/workimg/%Y/%m/%d',null=True)
    student=models.ForeignKey(Student)
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
    
    
    
    
    
        
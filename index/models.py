from django.db import models
from comment.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.auth.models import User
import os
# Create your models here.
class Order(models.Model):
    user_id=models.IntegerField()
    type=models.IntegerField(default=1)
    subject=models.CharField(max_length=200)
    out_trade_no=models.CharField(max_length=200)
    total_fee=models.FloatField()
    status=models.IntegerField(default=0)
    trade_no=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now=True)
    
class Profile(models.Model):
    type=models.IntegerField()
    sex=models.CharField(max_length=100)
    birth=models.DateField()
    province=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    img=models.ImageField(upload_to='img/%Y/%m/%d',default='touxiang.jpg')
    score=models.IntegerField(default=0)
    auth=models.IntegerField(default=0)
    auth_result=models.CharField(max_length=200)
    cert=models.ImageField(null=True,upload_to='cert/%Y/%m/%d')
    othercert=models.ImageField(null=True,blank=True,upload_to='cert/%Y/%m/%d')
    workshow=models.FileField(upload_to='cert/%Y/%m/%d',null=True,blank=True)
    user=models.OneToOneField(User)
    def getworksuffix(self):
        file_name_suffix=os.path.splitext(self.work.name)[1].lower()
        return file_name_suffix
class WorkType(models.Model):
    name=models.CharField(max_length=100)
    img=models.FileField(upload_to='worktype',null=True,blank=True)
    order=models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['order']
class Work(models.Model):
    name=models.CharField(max_length=100)
    worktype=models.ForeignKey(WorkType)
    desc=models.CharField(max_length=100)
    content=models.TextField()
    video=models.FileField(upload_to='work/%Y/%m/%d',null=True,blank=True)
    audio=models.FileField(upload_to='work/%Y/%m/%d',null=True,blank=True)
    image=models.ImageField(upload_to='work/%Y/%m/%d',null=True,blank=True)
    time=models.DateTimeField(auto_now=True)
    status=models.IntegerField(default=1)
    addit=models.TextField(null=True)
    app_sum=models.IntegerField(default=0)
    order=models.CharField(max_length=200)
    student=models.ForeignKey(Profile)
    def getorderid(self):
        order=Order.objects.get(out_trade_no=self.order)
        return order.id
    def getorderstatus(self):
        order=Order.objects.get(out_trade_no=self.order)
        return order.status
    def getorderfee(self):
        order=Order.objects.get(out_trade_no=self.order)
        return order.total_fee
    def getvideosuffix(self):
        file_name_suffix=os.path.splitext(self.video.name)[1].lower()
        return file_name_suffix
    def getaudiosuffix(self):
        file_name_suffix=os.path.splitext(self.audio.name)[1].lower()
        return file_name_suffix
class Applicate(models.Model):
    teacher=models.ForeignKey(Profile)
    time=models.DateTimeField(auto_now=True)
    stat=models.IntegerField()
    work=models.ForeignKey(Work)
class Comment(models.Model):
    content=models.TextField()
    video=models.FileField(upload_to='comment/%Y/%m/%d',null=True,blank=True)
    audio=models.FileField(upload_to='comment/%Y/%m/%d',null=True,blank=True)
    image=models.ImageField(upload_to='comment/%Y/%m/%d',null=True,blank=True)
    status=models.IntegerField(default=1)
    score=models.IntegerField(default=2)
    time=models.DateTimeField(auto_now=True)
    applicate=models.OneToOneField(Applicate)
    teacher=models.ForeignKey(Profile)
    def getvideosuffix(self):
        file_name_suffix=os.path.splitext(self.video.name)[1].lower()
        return file_name_suffix
    def getaudiosuffix(self):
        file_name_suffix=os.path.splitext(self.audio.name)[1].lower()
        return file_name_suffix
class Log(models.Model):
    content=models.TextField()
    time=models.DateTimeField(auto_now=True)
    profile=models.ForeignKey(Profile)
class Message(models.Model):
    content=models.TextField()
    time=models.DateTimeField(auto_now=True)
    obj=models.IntegerField()
    profile=models.ForeignKey(Profile)

    
    




    
    
    
    
    
        
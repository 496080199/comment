# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response, redirect
from index.forms import *
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    return render_to_response('index.html')

def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=User()
            user.username=form['username'].value()
            user.password=make_password(form['password2'].value())
            user.last_name=form['last_name'].value()
            user.first_name=form['first_name'].value()
            user.email=form['email'].value()
            user.is_active=1
            user.save()
            address=form['province'].value()+u'省'+form['city'].value()+u'市'+form['address'].value()
            if form['type'].value()=='teacher':
                teacher=Teacher(user=user)
                teacher.sex=form['sex'].value()
                teacher.birth=form['birth'].value()
                teacher.address=address
                teacher.phone=form['phone'].value()
                teacher.save()
            else:
                student=Student(user=user)
                student.sex=form['sex'].value()
                student.birth=form['birth'].value()
                student.address=address
                student.phone=form['phone'].value() 
                student.save()
            return redirect(reverse('index'))
    else:
        form=UserForm()
        
    return render(request,'register.html',{'form':form,})
def user_login(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form['username'].value()
            password=form['password'].value()
            user=authenticate(username=username,password=password)            
            #user=User.objects.get(username__exact=username,password__exact=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if user.teacher.id:
                        return redirect(reverse('teacher_center',args=(user.id,)))
                    elif user.student.id:
                        return redirect(reverse('student_center'))
    else:
        form=UserLoginForm()
    
    return render(request,'userlogin.html',{'form':form,})
def user_logout(request):
    logout(request)
    return redirect(reverse('user_login'))
def teacher_center(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    teacher=User.objects.get(id=id)
    img=teacher.teacher.img
    
    return render(request,'teacher_center.html',{'teacher':teacher})
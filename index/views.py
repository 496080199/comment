# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from index.forms import *
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from comment.settings import MEDIA_URL

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def logined(r):
    if r.user.is_authenticated():
        if Teacher.objects.filter(user_id=r.user.id):
            return redirect(reverse('teacher_center'))
        elif Student.objects.filter(user_id=r.user.id):
            return redirect(reverse('student_center'))
    return
def register(request):
    info=''
    if logined(request):
        return logined(request)
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
            if form['type'].value()=='teacher':
                teacher=Teacher(user=user)
                teacher.sex=form['sex'].value()
                teacher.birth=form['birth'].value()
                teacher.province=form['province'].value()
                teacher.city=form['city'].value()
                teacher.area=form['area'].value()
                teacher.address=form['address'].value()
                teacher.phone=form['phone'].value()
                teacher.save()
            else:
                student=Student(user=user)
                student.sex=form['sex'].value()
                student.birth=form['birth'].value()
                student.province=form['province'].value()
                student.city=form['city'].value()
                student.area=form['area'].value()
                student.address=form['address'].value()
                student.phone=form['phone'].value() 
                student.save()
            info='OK'
    else:
        form=UserForm()
        
    return render(request,'register.html',{'form':form,'info':info})
def user_login(request):
    if logined(request):
        return logined(request)
    #return HttpResponse(request.META['HTTP_REFERER'])
    error=[]
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
                    if Teacher.objects.filter(user_id=user.id):
                        address=reverse('teacher_center')
                        if request.META.has_key('HTTP_ORIGIN'):
                            address=request.META['HTTP_ORIGIN']
                        return redirect(address)

                    elif Student.objects.filter(user_id=user.id):
                            address=reverse('student_center')
                            if request.META.has_key('HTTP_ORIGIN'):
                                address=request.META['HTTP_ORIGIN']
                            return redirect(address)
            else:
                error.append('请输入正确的用户名和密码')
    else:
        form=UserLoginForm()
        
    
    return render(request,'userlogin.html',{'form':form,'error':error,})
def user_logout(request):
    logout(request)
    return redirect(reverse('user_login'))
def teacher_center(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    
    return render(request,'teacher_center.html',{'media_url':MEDIA_URL,'media_root':MEDIA_ROOT+'/'})
def student_center(request):
    
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    return render(request,'student_center.html',{'media_url':MEDIA_URL,'media_root':MEDIA_ROOT+'/'})

def change_password(request):
    
    info={}
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    user=request.user
    #return HttpResponse('OK')
    if request.method=='POST':
        form=UserChangePasswordForm(request.POST)
        if form.is_valid():
            oldpass=form['oldpass'].value()
            newpass=make_password(form['repeatpass'].value())
            if authenticate(username=user.username,password=oldpass):
                user.password=newpass
                user.save()
                info.setdefault('OK','修改成功')
            else:
                info.setdefault('ERR','请输入正确的密码')
    else:
        form=UserChangePasswordForm()
    return render(request,'changepassword.html',{'form':form,'info':info})

def change_info(request):
    info={}
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    user=request.user
    if request.method=='POST':
        form=UserChangeInfoForm(request.POST)
        #return HttpResponse(form)
        if form.is_valid():
            user.last_name=form['last_name'].value()
            user.first_name=form['first_name'].value()
            user.email=form['email'].value()
            user.save()
            if Teacher.objects.filter(user_id=user.id):
                user.teacher.sex=form['sex'].value()
                user.teacher.birth=form['birth'].value()
                user.teacher.province=form['province'].value()
                user.teacher.city=form['city'].value()
                user.teacher.area=form['area'].value()
                user.teacher.address=form['address'].value()
                user.teacher.phone=form['phone'].value()
                user.teacher.save()
            elif Student.objects.filter(user_id=user.id): 
                user.student.sex=form['sex'].value()
                user.student.birth=form['birth'].value()
                user.student.province=form['province'].value()
                user.student.city=form['city'].value()
                user.student.area=form['area'].value()
                user.student.address=form['address'].value()
                user.student.phone=form['phone'].value()
                user.student.save() 
            info.setdefault('OK','修改成功')
        else:
            info.setdefault('ERR','修改失败')
    else:
        if Teacher.objects.filter(user_id=user.id):
            form=UserChangeInfoForm({'last_name':user.last_name,'first_name':user.first_name,'email':user.email,'sex':user.teacher.sex,'birth':user.teacher.birth,'province':user.teacher.province,'city':user.teacher.city,'area':user.teacher.area,'address':user.teacher.address,'phone':user.teacher.phone})
        elif Student.objects.filter(user_id=user.id):
            form=UserChangeInfoForm({'last_name':user.last_name,'first_name':user.first_name,'email':user.email,'sex':user.student.sex,'birth':user.student.birth,'province':user.student.province,'city':user.student.city,'area':user.student.area,'address':user.student.address,'phone':user.student.phone})
    return render(request,'changeinfo.html',{'form':form,'info':info})
def to_answer(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    works=Work.objects.filter(status=1).exclude(applicate__teacher=request.user.teacher)
    #return HttpResponse(works)
    return render(request,'answer.html',{'works':works})
def show_answer(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    try:
        applicate=work.applicate_set.get(teacher_id=request.user.teacher.id)
    except Exception:
        applicate=None
    n=0
    if work.comment_set.filter(teacher=request.user.teacher):
        n=1
        
    
    return render(request,'show_answer.html',{'work':work,'id':id,'applicate':applicate,'media_url':MEDIA_URL,'media_root':MEDIA_ROOT+'/','n':n})
def app_answer(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    app=Applicate()
    app.work=work
    app.teacher=request.user.teacher
    app.stat=0
    app.save()
    return redirect(reverse('to_answer'))
def del_answer(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    app=request.user.teacher.applicate_set.filter(work=work)
    app.delete()
    return redirect(reverse('my_applicate'))
def my_applicate(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    apps=request.user.teacher.applicate_set.all()
    return render(request,'my_applicate.html',{'apps':apps}) 
def to_com(request,id):
    info=''
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            com=Comment()
            com.work=work
            com.teacher=request.user.teacher
            com.content=form['content'].value()
            com.file=form['file'].value()
            com.image=form['image'].value()
            com.status=1
            com.save()
            info='OK' 
            
    else:
        form=CommentForm()
    return render(request,'to_com.html',{'form':form,'work':work,'info':info})
def edit_com(request,id):
    info=''
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    com=request.user.teacher.comment_set.get(work=work)
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            com.content=form['content'].value()
            nfile=form['file'].value()
            if nfile is not None:
                if nfile==False:
                    if com.file:
                        os.remove(com.file.name)
                    com.file=None
                else:
                    if com.file:
                        os.remove(com.file.name)
                    com.file=nfile
            nimage=form['image'].value()
            if nimage is not None:
                if nimage==False:
                    if com.image:
                        os.remove(com.image.name)
                    com.image=None
                else:
                    if com.image:
                        os.remove(com.image.name)
                    com.image=nimage 
            com.save()
            info='OK'
    else:
        form=CommentForm(instance=com)
    return render(request,'edit_com.html',{'form':form,'work':work,'info':info})
def del_com(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    com=request.user.teacher.comment_set.get(work=work)
    if com.file:
        os.remove(com.file.name)
    if com.image:
        os.remove(com.image.name)
    com.delete()
    return redirect(reverse('show_answer',args=(id,)))
def to_ask(request):
    info=''
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    if request.method=='POST':
        form=WorkForm(request.POST,request.FILES)
        if form.is_valid():
            work=Work(student=request.user.student)
            work.name=form['name'].value()
            work.desc=form['desc'].value()
            work.content=form['content'].value()
            work.file=form['file'].value()
            work.image=form['image'].value()
            work.save()
            info='OK'    
    else:
        form=WorkForm()
    return render(request,'work_add.html',{'form':form,'info':info})
def my_ask(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    works=request.user.student.work_set.filter(status__gt=0)
    return render(request,'my_work.html',{'works':works})
def show_ask(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    n=0
    count=0
    if work.applicate_set.all():
        count=work.applicate_set.count()
        for app in work.applicate_set.all():
            if app.stat==True:
                n+=1
    return render(request,'show_work.html',{'work':work,'media_url':MEDIA_URL,'media_root':MEDIA_ROOT+'/','n':n,'count':count})
def manage_app(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    info=''
    work=Work.objects.get(id=id)
    apps=None
    if work.applicate_set.all():
        apps=work.applicate_set.all()
    if request.method=='POST':
        count=work.applicate_set.filter(stat=1).count()
        if count == 3:
            work.status=2
            work.save()
            for app in apps:
                if app.stat != 1:
                    app.stat=2
            return redirect(reverse('show_ask',args=(id,)))
        info='ERR'
    return render(request,'manage_app.html',{'apps':apps,'work':work,'info':info})
def auth_app(request,id,num):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    app=Applicate.objects.get(id=id)
    #return HttpResponse(app.stat)
    if int(num)==1:
        app.stat=1
    elif int(num)==0:
        app.stat=2
    app.save()
    return redirect(reverse('manage_app',args=(app.work.id,)))

def edit_ask(request,id):
    info=''
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    if request.method=='POST':
        form=WorkForm(request.POST,request.FILES)
        if form.is_valid():
            work.name=form['name'].value()
            work.desc=form['desc'].value()
            work.content=form['content'].value()
            nfile=form['file'].value()
            if nfile is not None:
                if nfile==False:
                    if work.file:
                        os.remove(work.file.name)
                    work.file=None
                else:
                    if work.file:
                        os.remove(work.file.name)
                    work.file=nfile
            nimage=form['image'].value()
            if nimage is not None:
                if nimage==False:
                    if work.image:
                        os.remove(work.image.name)
                    work.image=None
                else:
                    if work.image:
                        os.remove(work.image.name)
                    work.image=nimage 
            work.save()
            info='OK'
            
    else:
        form=WorkForm(instance=work)
    return render(request,'edit_ask.html',{'form':form,'info':info,'id':id})   
def addit_ask(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    if request.method=='POST':
        work.addit=request.POST['addit']
        work.save()
    return redirect(reverse('show_ask',args=(id,)))
        
def del_ask(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    Work.objects.filter(id=id).update(status=0)
    return redirect(reverse('my_ask'))

    
    
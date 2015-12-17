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
def change_img(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    user=request.user
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            if Teacher.objects.filter(user_id=user.id):
                user.teacher.img=form['img'].value()
                user.teacher.save()
            if Student.objects.filter(user_id=user.id):
                user.student.img=form['img'].value()
                user.student.save()
            return redirect(reverse('user_login'))
    else:
        form=ImgForm()
    return render(request,'change_img.html',{'form':form})
        
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
    works=Work.objects.filter(status=1).exclude(applicate__teacher=request.user.teacher).order_by('-time')
    #return HttpResponse(works)
    return render(request,'answer.html',{'works':works})
def show_answer(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    applicate=None
    try:
        applicate=request.user.teacher.applicate_set.get(work=work)
    except Exception:
        pass
    n=0
    try:
        com=applicate.comment
        if com:
            n=1
            if com.status==2:
                n=2
    except Exception:
        pass
        
    
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
    apps=request.user.teacher.applicate_set.all().order_by('-time')
    return render(request,'my_applicate.html',{'apps':apps}) 
def to_com(request,id):
    info=''
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    app=request.user.teacher.applicate_set.get(work=work)
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            com=Comment()
            com.work=work
            com.applicate=app
            com.content=form['content'].value()
            com.video=form['video'].value()
            com.audio=form['audio'].value()
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
    app=request.user.teacher.applicate_set.get(work=work)
    com=app.comment
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            com.content=form['content'].value()
            video=form['video'].value()
            if video is not None:
                if video==False:
                    if com.video:
                        os.remove(com.video.name)
                    com.video=None
                else:
                    if com.video:
                        os.remove(com.video.name)
                    com.video=video
            audio=form['audio'].value()
            if audio is not None:
                if audio==False:
                    if com.audio:
                        os.remove(com.audio.name)
                    com.audio=None
                else:
                    if com.audio:
                        os.remove(com.audio.name)
                    com.audio=audio
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
    app=request.user.teacher.applicate_set.get(work=work)
    com=app.comment
    if com.video:
        os.remove(com.video.name)
    if com.audio:
        os.remove(com.audio.name)
    if com.image:
        os.remove(com.image.name)
    com.delete()
    return redirect(reverse('show_answer',args=(id,)))
def submit_com(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    applicate=request.user.teacher.applicate_set.get(work=work)
    com=applicate.comment
    com.status=2
    com.save()
    apps=work.applicate_set.filter(stat=1)
    for app in apps:
        try:
            if app.comment.status!=2:
                return redirect(reverse('show_answer',args=(id,))) 
        except Exception:
            return redirect(reverse('show_answer',args=(id,))) 
    work.status=3
    work.save()
    return redirect(reverse('show_answer',args=(id,))) 
def view_com(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    apps=work.applicate_set.filter(stat=1)
    if request.method=='POST':
        work.status=4
        work.student.score+=5
        work.student.save()
        for app in apps:
            app.teacher.score+=app.comment.score
            app.teacher.save()
        work.save()
        return redirect(reverse('show_ask',args=(id,)))
    return render(request,'view_com.html',{'apps':apps,'work':work})
def score_com(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    com=Comment.objects.get(id=id)
    if request.method=='POST':
        score=request.POST['score']
        com.score=score
        com.save()
        return redirect(reverse('view_com',args=(com.applicate.work.id,)))
def to_ask(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    if request.method=='POST':
        form=WorkForm(request.POST,request.FILES)
        if form.is_valid():
            work=Work(student=request.user.student)
            work.name=form['name'].value()
            work.desc=form['desc'].value()
            work.content=form['content'].value()
            work.video=form['video'].value()
            work.audio=form['audio'].value()
            work.image=form['image'].value()
            work.save()   
    else:
        form=WorkForm()
    return render(request,'to_ask.html',{'form':form})
def my_ask(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    works=request.user.student.work_set.filter(status__gt=0).order_by('-time')
    return render(request,'my_ask.html',{'works':works})
def show_ask(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    n=0
    m=0
    com_count=0
    count=0
    if work.applicate_set.all():
        count=work.applicate_set.count()
        for app in work.applicate_set.all():
            if app.stat==True:
                n+=1
                try:
                     
                    if app.comment.status==2:
                        m+=1
                    
                except Exception:
                    pass
    com_count=count-m
    return render(request,'show_ask.html',{'work':work,'media_url':MEDIA_URL,'media_root':MEDIA_ROOT+'/','n':n,'count':count,'m':m,'com_count':com_count})
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
        if count <= 3 and count > 0 :
            work.status=2
            work.save()
            
            return redirect(reverse('show_ask',args=(id,)))
        info='ERR'
    return render(request,'manage_app.html',{'apps':apps,'work':work,'info':info})
def auth_app(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    app=Applicate.objects.get(id=id)
    if request.method=='POST':
        stat=request.POST['stat']
        app.stat=stat
        app.save()#return HttpResponse(app.stat)
    
    return redirect(reverse('manage_app',args=(app.work.id,)))

def edit_ask(request,id):
    info=''
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    if request.method=='POST':
        form=WorkForm(request.POST,request.FILES)
        #if form.is_valid():
        work.name=form['name'].value()
        work.desc=form['desc'].value()
        work.content=form['content'].value()
        video=form['video'].value()
        if video:
            if work.video:
                os.remove(work.video.name)
            work.video=video
        audio=form['audio'].value()
        if audio:
            if work.audio:
                os.remove(work.audio.name)
            work.audio=audio
        image=form['image'].value()
        if image:
            if work.image:
                os.remove(work.image.name)
            work.image=image
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

    
    
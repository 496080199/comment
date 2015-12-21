# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from index.forms import *
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from comment.settings import MEDIA_URL
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def logined(r):
    if r.user.is_authenticated():
        if r.user.profile.type==1:
            return redirect(reverse('teacher_center'))
        elif r.user.profile.type==2:
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
            profile=Profile(user=user)
            profile.type=form['type'].value()
            profile.sex=form['sex'].value()
            profile.birth=form['birth'].value()
            profile.province=form['province'].value()
            profile.city=form['city'].value()
            profile.area=form['area'].value()
            profile.address=form['address'].value()
            profile.phone=form['phone'].value()
            profile.type=form['type'].value()
            profile.save()
            log(profile,"成功注册了账号")
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
                    return logined(request)
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
    
    return render(request,'teacher_center.html',{'media_url':MEDIA_URL})
def auth_teacher(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    teacher=request.user.profile
    if request.method=='POST':
        form=AuthForm(request.POST,request.FILES)
        if form.is_valid():
            if teacher.auth==2:
                teacher.auth=0
            teacher.cert=form['cert'].value()
            teacher.othercert=form['othercert'].value()
            teacher.work=form['work'].value()
            teacher.save()
            return redirect(reverse('user_login'))
    else:
        form=AuthForm({'cert':teacher.cert,'othercert':teacher.othercert,'workshow':teacher.workshow})
    return render(request,'auth_teacher.html',{'form':form,'media_url':MEDIA_URL,})
def view_teacher(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    teacher=Profile.objects.get(id=id)
    apps=teacher.applicate_set.filter(stat=1)
    coms=0
    for app in apps:
        if app.comment.status==2:
            coms+=1
    return render(request,'view_teacher.html',{'teacher':teacher,'coms':coms,'media_url':MEDIA_URL})
def change_img(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    user=request.user
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            user.profile.img=form['img'].value()
            user.profile.save()
            return redirect(reverse('user_login'))
    else:
        form=ImgForm()
    return render(request,'change_img.html',{'form':form})
        
def student_center(request):
    
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    return render(request,'student_center.html',{'media_url':MEDIA_URL})

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
            user.profile.sex=form['sex'].value()
            user.profile.birth=form['birth'].value()
            user.profile.province=form['province'].value()
            user.profile.city=form['city'].value()
            user.profile.area=form['area'].value()
            user.profile.address=form['address'].value()
            user.profile.phone=form['phone'].value()
            user.profile.save()
            info.setdefault('OK','修改成功')
        else:
            info.setdefault('ERR','修改失败')
    else:
        form=UserChangeInfoForm({'last_name':user.last_name,'first_name':user.first_name,'email':user.email,'sex':user.profile.sex,'birth':user.profile.birth,'province':user.profile.province,'city':user.profile.city,'area':user.profile.area,'address':user.profile.address,'phone':user.profile.phone})
    return render(request,'changeinfo.html',{'form':form,'info':info})
def to_answer(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    works=Work.objects.filter(status=1).exclude(applicate__teacher=request.user.profile).order_by('-time')
    #return HttpResponse(works)
    return render(request,'answer.html',{'works':works})
def show_answer(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    applicate=None
    try:
        applicate=request.user.profile.applicate_set.get(work=work)
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
        
    
    return render(request,'show_answer.html',{'work':work,'id':id,'applicate':applicate,'media_url':MEDIA_URL,'n':n})
def app_answer(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    if request.user.profile.auth!=1:
        return redirect(reverse('auth_teacher'))
    work=Work.objects.get(id=id)
    app=Applicate()
    app.work=work
    app.teacher=request.user.profile
    app.stat=0
    app.save()
    return redirect(reverse('my_applicate'))
def del_answer(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    app=request.user.profile.applicate_set.filter(work=work)
    app.delete()
    return redirect(reverse('my_applicate'))
def my_applicate(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    apps=request.user.profile.applicate_set.all().order_by('-time')
    return render(request,'my_applicate.html',{'apps':apps}) 
def to_com(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    app=request.user.profile.applicate_set.get(work=work)
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            com=Comment()
            com.work=work
            com.applicate=app
            com.teacher=request.user.profile
            com.content=form['content'].value()
            com.video=form['video'].value()
            com.audio=form['audio'].value()
            com.image=form['image'].value()
            com.status=1
            com.save()
            
    else:
        form=CommentForm()
    return render(request,'to_com.html',{'form':form,'work':work,'id':id,})

def edit_com(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    app=request.user.profile.applicate_set.get(work=work)
    com=app.comment
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            com.content=form['content'].value()
            video=form['video'].value()
            if video:
                if com.video:
                    os.remove(com.video.name)
                com.video=video
            elif video==False:
                if com.video:
                    os.remove(com.video.name)
                com.video=None
            audio=form['audio'].value()
            if audio:
                if com.audio:
                    os.remove(com.audio.name)
                com.audio=audio
            elif audio==False:
                if com.audio:
                    os.remove(com.audio.name)
                com.audio=None
            image=form['image'].value()
            if image:
                if com.image:
                    os.remove(com.image.name)
                com.image=image
            elif image==False:
                if com.image:
                    os.remove(com.image.name)
                com.image=None
            com.save()
    else:
        form=CommentForm(instance=com)
    return render(request,'edit_com.html',{'form':form,'work':work,'id':id})
def del_com(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    app=request.user.profile.applicate_set.get(work=work)
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
    applicate=request.user.profile.applicate_set.get(work=work)
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
    info=''
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=request.user.profile.work_set.get(id=id)
    apps=work.applicate_set.filter(stat=1)
    if request.method=='POST':
        scores=0
        for app in apps:
            scores+=app.comment.score
        if int(scores) == 10:
            work.status=4
            work.student.score+=10
            work.student.save()
            for app in apps:
                app.teacher.score+=app.comment.score
                app.teacher.save()
            work.save()
            return redirect(reverse('show_ask',args=(id,)))
        else:
            info='ERR'
    return render(request,'view_com.html',{'apps':apps,'work':work,'info':info,'media_url':MEDIA_URL,})
def to_ask(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    if request.method=='POST':
        
        form=WorkForm(request.POST,request.FILES)
        if form.is_valid():
            work=Work(student=request.user.profile)
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
    works=request.user.profile.work_set.filter(status__gt=0).order_by('-time')
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
    return render(request,'show_ask.html',{'work':work,'media_url':MEDIA_URL,'n':n,'count':count,'m':m,'com_count':com_count})
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


def edit_ask(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    if request.method=='POST':
        form=WorkForm(request.POST,request.FILES)
        if form.is_valid():
            work.name=form['name'].value()
            work.desc=form['desc'].value()
            work.content=form['content'].value()
            video=form['video'].value()
            if video:
                if work.video:
                    os.remove(work.video.name)
                work.video=video
            elif video==False:
                if work.video:
                    os.remove(work.video.name)
                work.video=None
            audio=form['audio'].value()
            if audio:
                if work.audio:
                    os.remove(work.audio.name)
                work.audio=audio
            elif audio==False:
                if work.audio:
                    os.remove(work.audio.name)
                work.audio=None
            image=form['image'].value()
            if image:
                if work.image:
                    os.remove(work.image.name)
                work.image=image
            elif image==False:
                if work.image:
                    os.remove(work.image.name)
                work.image=None
            work.save()
            
    else:
        form=WorkForm(instance=work)
    return render(request,'edit_ask.html',{'form':form,'id':id})   
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
    work=Work.objects.get(id=id)
    work.status=0
    work.save(update_fields=['status'])
    apps=work.applicate_set.all()
    for app in apps:
        app.delete()
    return redirect(reverse('my_ask'))
def change_app_stat(request,id,val):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    app=Applicate.objects.get(id=id)
    if app.work.status==1:
        if request.is_ajax():
            app.stat=int(val)
            app.save(update_fields=['stat'])
            return HttpResponse('OK')
    return HttpResponse('ERR')
    
def change_com_score(request,id,val):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    com=Comment.objects.get(id=id)
    if com.applicate.work.status==3:
        if request.is_ajax():
            com.score=int(val)
            com.save(update_fields=['score'])
            return HttpResponse('OK')
    return HttpResponse('ERR')

def log(profile,action):
    log=Log()
    log.profile=profile
    log.content=str(action)
    log.save()
    return 'OK'
    
    
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from index.forms import *
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from comment.settings import MEDIA_URL, ALIPAY,RETURN_URL,NOTIFY_URL, FROM_EMAIL
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from alipay import Alipay
import httplib2
from django.views.decorators.csrf import csrf_exempt
from django.views.csrf import csrf_failure
from urllib import urlencode
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.
def index(request):
    types=WorkType.objects.all().order_by('order')[:6]
    logs=Log.objects.all().order_by('-time')[:3]
    works=Work.objects.filter(status=1).order_by('-time')[:3]
    #return HttpResponse(types[0])
    
    return render(request,'index.html',{'logs':logs,'works':works,'types':types,'media_url':MEDIA_URL})
def more_type(request):
    types=WorkType.objects.all().order_by('order')
    page_size=8
    paginator=Paginator(types,page_size)
    try:
        page=int(request.GET.get('page','1'))
    except ValueError:
       page=1
    try:
        type_list=paginator.page(page)
    except (EmptyPage,InvalidPage):
        type_list=paginator.page(paginator.num_pages)
    return render(request,'more_type.html',{'type_list':type_list,'media_url':MEDIA_URL})
def more_ask(request):
    works=Work.objects.filter(status=1).order_by('-time')
    page_size=8
    paginator=Paginator(works,page_size)
    try:
        page=int(request.GET.get('page','1'))
    except ValueError:
       page=1
    try:
        work_list=paginator.page(page)
    except (EmptyPage,InvalidPage):
        work_list=paginator.page(paginator.num_pages)
    return render(request,'more_ask.html',{'work_list':work_list})
def top_teacher(request):
    teachers=Profile.objects.filter(type=1).order_by('-score')
    page_size=8
    paginator=Paginator(teachers,page_size)
    try:
        page=int(request.GET.get('page','1'))
    except ValueError:
       page=1
    try:
        teacher_list=paginator.page(page)
    except (EmptyPage,InvalidPage):
        teacher_list=paginator.page(paginator.num_pages)
    return render(request,'top_teacher.html',{'teacher_list':teacher_list,'media_url':MEDIA_URL})
    
def hot_ask(request):
    works=Work.objects.filter(status=1).order_by('-app_sum')
    page_size=15
    paginator=Paginator(works,page_size)
    try:
        page=int(request.GET.get('page','1'))
    except ValueError:
       page=1
    try:
        work_list=paginator.page(page)
    except (EmptyPage,InvalidPage):
        work_list=paginator.page(paginator.num_pages)
    return render(request,'hot_ask.html',{'work_list':work_list})
def more_log(request):
    logs=Log.objects.all().order_by('-time')
    page_size=15
    paginator=Paginator(logs,page_size)
    try:
        page=int(request.GET.get('page','1'))
    except ValueError:
        page=1
    try:
        log_list=paginator.page(page)
    except (EmptyPage,InvalidPage):
        log_list=paginator.page(paginator.num_pages)
    return render(request,'more_log.html',{'log_list':log_list})

def view_worktype(request,id):
    worktype=WorkType.objects.get(id=id)
    works=worktype.work_set.filter(status=1).order_by('-time')
    page_size=15
    paginator=Paginator(works,page_size)
    try:
        page=int(request.GET.get('page','1'))
    except ValueError:
        page=1
    try:
        work_list=paginator.page(page)
    except (EmptyPage,InvalidPage):
        work_list=paginator.page(paginator.num_pages)
    
    return render(request,'view_worktype.html',{'work_list':work_list,'worktype':worktype})
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
def forget_password(request):
    info=''
    if request.method=='POST':
        email=request.POST['email']
        user=User.objects.get(email=email)
        password=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
        user.password=make_password(password)
        user.save()
        send_mail('重置密码','您的新密码为：'+password+',请登录后及时修改密码,谢谢。',FROM_EMAIL,[email])
        info='OK'
    return render(request,'forget_password.html',{'info':info})
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
                    log(request.user.profile,"登陆了系统")    
                    return logined(request)
            else:
                error.append('请输入正确的用户名和密码')
    else:
        form=UserLoginForm()
        
    
    return render(request,'userlogin.html',{'form':form,'error':error,})
def user_logout(request):
    log(request.user.profile,"退出了系统") 
    logout(request)
    return redirect(reverse('user_login'))
def teacher_center(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    msg_count=Message.objects.filter(obj=request.user.profile.id).filter(status=1).count()
    
    return render(request,'teacher_center.html',{'media_url':MEDIA_URL,'msg_count':msg_count})
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
    coms=teacher.comment_set.filter(status=2).count()
    return render(request,'view_teacher.html',{'teacher':teacher,'coms':coms,'media_url':MEDIA_URL})
def view_student(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    student=Profile.objects.get(id=id)
    asks=student.work_set.filter(status=4).count()
    return render(request,'view_student.html',{'student':student,'asks':asks,'media_url':MEDIA_URL})
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
    msg_count=Message.objects.filter(obj=request.user.profile.id).filter(status=1).count()
    return render(request,'student_center.html',{'media_url':MEDIA_URL,'msg_count':msg_count})

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
    work.app_sum+=1
    work.save()
    message(request.user.profile,"发起了解答申请,问题是：",work.id,work.student.id)
    return redirect(reverse('my_applicate'))
def del_answer(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=Work.objects.get(id=id)
    app=request.user.profile.applicate_set.filter(work=work)
    app.delete()
    work.app_sum-=1
    work.save()
    message(request.user.profile,"删除了解答申请,问题是：",work.id,work.student.id)
    return redirect(reverse('my_applicate'))
def my_applicate(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    apps=request.user.profile.applicate_set.filter(work__status=1).order_by('-time')
    return render(request,'my_applicate.html',{'apps':apps}) 
def my_comment(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    apps=request.user.profile.applicate_set.filter(work__status__gt=1).order_by('-time')
    return render(request,'my_comment.html',{'apps':apps}) 
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
    com=request.user.profile.comment_set.get(work=work)
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
    com=request.user.profile.applicate_set.get(work=work).comment
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
    message(request.user.profile,"提交了解答,解答的问题是：",work.id,work.student.id)
    return redirect(reverse('show_answer',args=(id,))) 
def view_com(request,id):
    info=''
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    work=request.user.profile.work_set.get(id=id)
    apps=work.applicate_set.filter(stat=1)
    order=None
    if work.order:
        order=Order.objects.get(out_trade_no=work.order)
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
                if work.order:
                    neworder=Order(user_id=app.teacher.user.id)
                    neworder.type=2
                    neworder.subject=work.name+u'的解答费'
                    neworder.total_fee=round(float(app.comment.score)/10*(order.price),2)
                    neworder.price=0
                    neworder.charge=0
                    neworder.save()
                
                message(request.user.profile,"给您评了"+str(app.comment.score)+"分，问题是：",work.id,app.teacher.id)
            work.save()
            return redirect(reverse('show_ask',args=(id,)))
        else:
            info='ERR'
    return render(request,'view_com.html',{'apps':apps,'work':work,'order':order,'info':info,'media_url':MEDIA_URL,})
def to_ask(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    if request.method=='POST':
        
        form=WorkForm(request.POST,request.FILES)
        if form.is_valid():
            work=Work(student=request.user.profile)
            work.name=form['name'].value()
            work.worktype_id=int(form['worktype'].value())
            work.desc=form['desc'].value()
            work.content=form['content'].value()
            work.video=form['video'].value()
            work.audio=form['audio'].value()
            work.image=form['image'].value()
            work.save() 
            if form['pay'].value()=='1':
                order=Order()
                order.user_id=request.user.id
                order.subject=work.name+u'的提问费'
                price=float(form['price'].value())
                if price:
                    order.total_fee=round(price,2)
                    order.charge=round(price*0.02,2)
                    order.price=round(price*(1-0.02),2)
                else:
                    order.total_fee=10.0
                    order.charge=0.2
                    order.price=9.8
                    
                    
                order.save()
                work.order=order.out_trade_no
                work.save()
                  
            log(request.user.profile,"发布了一个问题")
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
    work=request.user.profile.work_set.get(id=id)
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
            for app in work.applicate_set.filter(stat=1):
                message(request.user.profile,"同意了您的申请，问题是：",work.id,app.teacher.id)
            
            return redirect(reverse('show_ask',args=(id,)))
        info='ERR'
    else:
        if work.order:
            order=Order.objects.get(out_trade_no=work.order)
            if order.status!=1:
                return redirect(reverse('view_order',args=(order.id,)))
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
        for app in work.applicate_set.filter(stat=1):
            message(request.user.profile,"补充了说明，问题是：",work.id,app.teacher.id)
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
        message(request.user.profile,"删了一个问题,问题是：",work.id,app.teacher.id)
    return redirect(reverse('my_ask'))
def change_app_stat(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    app=Applicate.objects.get(id=id)
    if app.work.status==1:
        if request.method=='POST':
            val=request.POST['stat']
            app.stat=int(val)
            app.save(update_fields=['stat'])
            return HttpResponse('OK')
    return HttpResponse('ERR')
    
def change_com_score(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    com=Comment.objects.get(id=id)
    if com.applicate.work.status==3:
        if request.method=='POST':
            val=request.POST['score']
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
def message(profile,action,work_id,profile_id):
    message=Message()
    message.profile=profile
    message.content=str(action)
    message.work_id=work_id
    message.obj=profile_id
    message.save()
    return 'OK'
def view_message(request):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    messages=Message.objects.filter(obj=request.user.profile.id).order_by('-time')
    return render(request,'view_message.html',{'messages':messages})
def message_redirect(request,m_id,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    message=Message.objects.get(id=m_id)
    if message.status==1:
        message.status=0
        message.save()
    if request.user.profile.type==1:
        return redirect(reverse('show_answer',args=(id,)))
    elif request.user.profile.type==2:
        return redirect(reverse('show_ask',args=(id,)))    
    

def my_order(request,type):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    info=''
    orders=Order.objects.filter(user_id=request.user.id).filter(status=type).exclude(batch_id=1).order_by('-time')
    total=0.0
    for order in orders:
        total+=order.total_fee
    if request.method=='POST': 
        if int(type)==0 and request.user.profile.type==1 and total > 0:
            neworder=Order()
            neworder.user_id=request.user.id
            neworder.subject=request.user.last_name+request.user.last_name+u'老师解答批量收款'
            neworder.total_fee=round(float(total),2)
            neworder.status=2
            neworder.type=2
            neworder.batch_id=1
            neworder.price=0
            neworder.charge=0
            neworder.save()
            for order in orders:
                order.batch_id=neworder.out_trade_no
                order.status=2
                order.save()
                info='OK'
        else:
            info='ERR'
            
        
    return render(request,'my_order.html',{'orders':orders,'type':int(type),'total':total,'info':info})
def view_order(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    order=Order.objects.get(id=id)
    return render(request,'view_order.html',{'order':order,})
def to_pay(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    order=Order.objects.get(id=id)
    pay_url=ALIPAY.create_direct_pay_by_user_url(out_trade_no=order.out_trade_no, subject=order.subject, total_fee=str(order.total_fee), return_url=RETURN_URL, notify_url=NOTIFY_URL)
    return redirect(pay_url)
@csrf_exempt
def pay_notify(request):
    param=request.POST.dict()
    if ALIPAY.verify_notify(**param):
        out_trade_no=param['out_trade_no']
        trade_no=param['trade_no']
        total_fee=param['total_fee']
        trade_status=param['trade_status']
        order=Order.objects.get(out_trade_no=out_trade_no)
        if str(order.total_fee)==total_fee: 
            if trade_status=='TRADE_FINISHED':
                print 'TRADE_FINISHED'
                if order.status!=1:
                    order.status=1
                    order.trade_no=trade_no
                    order.save()
                return HttpResponse('通知正常')
            elif  trade_status=='TRADE_SUCCESS':
                print 'TRADE_SUCCESS'
                if order.status!=1:
                    order.status=1
                    order.trade_no=trade_no
                    order.save()
                return HttpResponse('通知正常')
    else:
        print 'ERR'
        return HttpResponse('通知不正确')

def pay_return(request):
    param=request.GET
    out_trade_no=param['out_trade_no']
    work=Work.objects.get(order=out_trade_no)
    return redirect(reverse('manage_app',args=(work.id,)))

def app_pay(request,id):
    if not request.user.is_authenticated():
        return redirect(reverse('user_login'))
    if request.method=='POST':
        order=Order.objects.get(id=id)
        if order.status!=2:
            order.status=2
            order.save()
    return redirect(reverse('view_order',args=(id,)))
        
    
    
    
    
    
    
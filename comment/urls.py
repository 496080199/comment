"""comment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static  
from django.conf import settings

urlpatterns = [
    url(r'^$','index.views.index',name='index'),
    url(r'^register$','index.views.register',name='register'),
    url(r'^user_login$','index.views.user_login',name='user_login'),
    url(r'^user_logout$','index.views.user_logout',name='user_logout'),
    url(r'^teacher_center$','index.views.teacher_center',name='teacher_center'),
    url(r'^student_center$','index.views.student_center',name='student_center'),
    url(r'^change_password$','index.views.change_password',name='change_password'),
    url(r'^change_info$','index.views.change_info',name='change_info'),
    url(r'^to_answer$','index.views.to_answer',name='to_answer'),
    url(r'^show_answer/([0-9]+)$','index.views.show_answer',name='show_answer'),
    url(r'^app_answer/([0-9]+)$','index.views.app_answer',name='app_answer'),
    url(r'^del_answer/([0-9]+)$','index.views.del_answer',name='del_answer'),
    url(r'^my_applicate$','index.views.my_applicate',name='my_applicate'),
    url(r'^to_ask$','index.views.to_ask',name='to_ask'),
    url(r'^my_ask$','index.views.my_ask',name='my_ask'),
    url(r'^manage_app/([0-9]+)$','index.views.manage_app',name='manage_app'),
    url(r'^auth_app/([0-9]+)$','index.views.auth_app',name='auth_app'),
    url(r'^show_ask/([0-9]+)$','index.views.show_ask',name='show_ask'),
    url(r'^edit_ask/([0-9]+)$','index.views.edit_ask',name='edit_ask'),
    url(r'^addit_ask/([0-9]+)$','index.views.addit_ask',name='addit_ask'),
    url(r'^del_ask/([0-9]+)$','index.views.del_ask',name='del_ask'),
    url(r'^to_com/([0-9]+)$','index.views.to_com',name='to_com'),
    url(r'^edit_com/([0-9]+)$','index.views.edit_com',name='edit_com'),
    url(r'^del_com/([0-9]+)$','index.views.del_com',name='del_com'),
    url(r'^submit_com/([0-9]+)$','index.views.submit_com',name='submit_com'),
    url(r'^view_com/([0-9]+)$','index.views.view_com',name='view_com'),
    url(r'^score_com/([0-9]+)$','index.views.score_com',name='score_com'),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT) 

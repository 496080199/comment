# -*- coding: utf-8 -*-
from index.models import *
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
#from captcha.fields import *


class UserForm(ModelForm):
    
    type_list=(
            ('student','学生'),
            ('teacher','老师'),
            )
    sex_list=(
            ('男','男'),
            ('女','女'),
            )
    password1=forms.CharField(label='密码',widget=forms.PasswordInput)
    password2=forms.CharField(label='重复输入密码',widget=forms.PasswordInput)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    sex=forms.ChoiceField(choices=sex_list)
    birth=forms.DateField(widget=forms.DateInput)
    province=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    area=forms.CharField(max_length=100)
    address=forms.CharField(max_length=500)
    phone=forms.CharField(max_length=100)
    type=forms.ChoiceField(choices=type_list)
    #captcha=CaptchaField()
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        phone =cleaned_data.get("phone")
        if password1 and password2:
            if password1!=password2:
                msg = u"两个密码不一致。"
                self._errors["password2"] = self.error_class([msg])
        if phone:
            if len(phone)!=11 or not phone.startswith('1'):
                msg=u"您输入的电话号码有误"
                self._errors["phone"] = self.error_class([msg])  
        return cleaned_data
    class Meta:
        model=User
        fields='username','password1','password2','first_name','last_name','email','sex','birth','province','city','address','phone','type'
class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
class UserChangePasswordForm(forms.Form):
    oldpass=forms.CharField(widget=forms.PasswordInput)
    newpass=forms.CharField(widget=forms.PasswordInput)
    repeatpass=forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super(UserChangePasswordForm, self).clean()
        newpass = cleaned_data.get("newpass")
        repeatpass = cleaned_data.get("repeatpass")
        if newpass and repeatpass:
            if newpass!=repeatpass:
                msg = u"两个新密码不一致。"
                self._errors["repeatpass"] = self.error_class([msg])
class UserChangeInfoForm(forms.Form):
    sex_list=(
            ('男','男'),
            ('女','女'),
            )
    last_name=forms.CharField(max_length=100)
    first_name=forms.CharField(max_length=100)
    email=forms.EmailField()
    sex=forms.ChoiceField(choices=sex_list)
    birth=forms.DateField(widget=forms.DateInput)
    province=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)
    area=forms.CharField(max_length=100)
    address=forms.CharField(max_length=500)
    phone=forms.CharField(max_length=100)
    def clean(self):
        cleaned_data = super(UserChangeInfoForm, self).clean()
        phone =cleaned_data.get("phone")
        if phone:
            if len(phone)!=11 or not phone.startswith('1'):
                msg=u"您输入的电话号码有误"
                self._errors["phone"] = self.error_class([msg])  
        return cleaned_data
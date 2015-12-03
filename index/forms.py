# -*- coding: utf-8 -*-
from index.models import *
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

class UserForm(ModelForm):
    type_list=(
            ('teacher','老师'),
            ('student','学生'),
            )
    sex_list=(
            ('male','男'),
            ('female','女'),
            )
    sex=forms.ChoiceField(choices=sex_list)
    birth=forms.DateField()
    province=forms.CharField(max_length=50)
    city=forms.CharField(max_length=50)
    address=forms.CharField(max_length=500)
    phone=forms.IntegerField()
    type=forms.ChoiceField(choices=type_list)
    class Meta:
        model=User
        fields='username','password','first_name','last_name','email','sex','birth','address','phone','type'
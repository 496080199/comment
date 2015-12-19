from django.contrib import admin
from django.contrib.auth.models import User
from .models import Teacher,Student
# Register your models here.

class TeacherInline(admin.StackedInline):
    model=Teacher
#class StudentInline(admin.TabularInline):
#    model=Student
class UserAdmin(admin.ModelAdmin):
    
    inlines=[TeacherInline]
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
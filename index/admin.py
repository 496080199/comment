from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile,Order
# Register your models here.

class ProfileInline(admin.StackedInline):
    model=Profile
#class StudentInline(admin.TabularInline):
#    model=Student
class UserAdmin(admin.ModelAdmin):
    
    inlines=[ProfileInline]
    
class OrderAdmin(admin.ModelAdmin):
    list_display=('subject','out_trade_no','total_fee','status','type','user_id')
    search_fields = ['subject']
    list_editable = ('subject',)
    list_filter = ('type','user_id','status','batch_id')
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Order,OrderAdmin)
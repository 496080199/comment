from django.shortcuts import render,render_to_response
from index.forms import *
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return render_to_response('index.html')

def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        return HttpResponse(form)
    else:
        form=UserForm()
        
    return render(request,'register.html',{'form':form,})
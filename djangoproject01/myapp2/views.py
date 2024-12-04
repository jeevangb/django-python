from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
import datetime

# Create your views here.
def my_view(request):
    dt=datetime.datetime.now()
    return render(request,'date.html',{'dt':dt})

def emp_details(request):
    eno=123
    ename="jeevan"
    detais={'eno':eno,'ename':ename}
    return render(request,'emp.html',detais)

def v1(request):
    return render(request,'index.html',{'name':'jeevan','age':23})

def v2(request):
    return render(request,'index1.html')
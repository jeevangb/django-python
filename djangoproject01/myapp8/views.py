from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'myhome.html')
def emp_details(request):
    return render(request,'display.html')
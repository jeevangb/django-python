from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request,'home.html')

def add(request):
    a=int(request.POST['Num1'])
    b=int(request.POST['Num2'])
    result=a+b
    return render(request,'result.html',{'result':result})
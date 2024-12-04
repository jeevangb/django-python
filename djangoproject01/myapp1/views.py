from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def v1(request):
    return HttpResponse("This is my first view from myapp1")

def v2(request):
    return HttpResponse("This is my second view from myapp1")


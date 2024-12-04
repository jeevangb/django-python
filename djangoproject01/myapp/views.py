from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def v1(request):
    return  HttpResponse("<h1>This is my first view<h1>")

def v2(request):
    return HttpResponse("<h1>This is my second view<h1>")

def v3(request):
     return HttpResponse("<h1>This is my third view<h1>")
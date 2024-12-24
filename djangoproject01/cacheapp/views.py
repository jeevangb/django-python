from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
# @cache_page(30) also possible through urls
def v1(request):
    return render(request,'mycache.html')

def v2(request):
    return render(request,'mycache1.html')

def v3(request):
    return render(request,'mycache2.html')
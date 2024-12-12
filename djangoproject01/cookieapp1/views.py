from django.shortcuts import render

# Create your views here.
def set_cookies(request):
    response=render(request,'set.html')
    response.set_cookie('name','jeevan',max_age=120)
    return  response

def get_cookies(request):
    cookiedata=request.COOKIES.get('name','no cookies data ')
    return  render(request,'get.html',{'cookiedata':cookiedata})

def del_cookies(request):
    response=render(request,'del.html')
    response.delete_cookie('name')
    return response
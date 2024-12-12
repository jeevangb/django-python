from datetime import datetime, timedelta

from django.http import HttpResponse
# Create your views here.
def set_cookie(request):
    response=HttpResponse("Cookie is set")
    # response.set_cookie("name","techSQuad",max_age=60)
    response.set_cookie('name', 'techSQuad', expires=datetime.utcnow() + timedelta(days=4))
    return response

def get_cookie(request):
    # cookiedata=request.COOKIES['name']
    cookiedata=request.COOKIES.get('name',"No cookies data")
    return HttpResponse("The cookie data is "+cookiedata)

def del_cookies(request):
    response = HttpResponse("cookie data is deleted")
    response.delete_cookie('name')
    return  response
from django.shortcuts import render, HttpResponse

# Create your views here.
def set_session(request):
    request.session['name']="mohan"
    return render(request,'set.html')

def get_session(request):
    if 'name' in request.session:
        name=request.session['name']
        request.session.modified=True
        return  render(request,'get.html',{'name':name})
    else:
        return HttpResponse("Session has expired")
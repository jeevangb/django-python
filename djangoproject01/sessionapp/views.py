from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['city']='Bangalore'
    return  render(request,'set.html')

def get_session(request):
    # session_data=request.session['city']
    session_data=request.session.get('city',default='no session data')
    session_age=request.session.get_expiry_age()
    session_date=request.session.get_expiry_date()
    return  render(request,'get.html',{'session_data':session_data,'session_age':session_age,'session_date':session_date})

def del_session(request):
    # if 'city' in request.session:
    #     del request.session['city']
    request.session.flush()
    print(request.session.get_expire_at_browser_close())
    request.session.clear_expired()
    return render(request,'del.html')
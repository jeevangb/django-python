from django.shortcuts import render
from authenticationapp.forms import SignUpForm
# Create your views here.
def sign_up(request):
    fm=SignUpForm()
    return render(request,'signup.html',{'form':fm})
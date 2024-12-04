from django.shortcuts import render
from myapp7.forms import StudentForm
from myapp7.models import Student
from django.contrib import messages
# Create your views here.
def emp_view(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            age = fm.cleaned_data['age']
            address = fm.cleaned_data['address']
            mail = fm.cleaned_data['mail']
            s=Student(name=name,age=age,address=address,mail=mail)
            s.save()
            messages.add_message(request,messages.SUCCESS,"Student details inserted successfully")
        else:
            messages.info(request,'Invalid data ')
    else:
        fm = StudentForm()
    return render(request,'mystudent1.html',{'form':fm})
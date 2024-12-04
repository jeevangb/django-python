from django.shortcuts import render
from myapp6.forms import EmployeeForm
from myapp6.models import Employee
from django.contrib import messages
# Create your views here.

def emp_view(request):
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            address=fm.cleaned_data['address']
            mail = fm.cleaned_data['mail']
            age = fm.cleaned_data['age']
            #for insert data
            # e=Employee(name=name,address=address,mail=mail,age=age)
            # e.save()
            # messages.add_message(request, messages.SUCCESS, 'Employee has been successfully created')

            #for update data
            # e=Employee(id=1,name=name,address=address,mail=mail,age=age)
            # e.save()
            # messages.add_message(request,messages.SUCCESS,'Employee data updated successfully')

            #for delete
            e = Employee(id=3)
            e.delete()
            messages.add_message(request,messages.SUCCESS,'Employee data deleted successfully')
        else:
            messages.info(request, 'Please enter valid details')
    else:
        fm = EmployeeForm()
    return render(request,'employee1.html',{'form':fm})
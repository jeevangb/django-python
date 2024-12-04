from django.shortcuts import render
from myapp5.forms import EmployeeForm

# Create your views here.
def emp_view(request):
  if request.method == 'POST':
      fm=EmployeeForm(request.POST )
      if fm.is_valid():
          print(fm.cleaned_data['name'])
          print(fm.cleaned_data['address'])
          print(fm.cleaned_data['mail'])
          print(fm.cleaned_data['age'])
          print(fm.cleaned_data['password'])
          print(fm.cleaned_data['retype_password'])
          print("fm data is submitted")
      else:
        print("please enter values")
  else:
    fm = EmployeeForm()
  # fm.order_fields(field_order=['address','age','name','mail'])
  return  render(request,'employee.html',{'form':fm})
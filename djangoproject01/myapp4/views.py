from django.shortcuts import render

from myapp4.models import Student


# Create your views here.

def student_view(request):
    students = Student.objects.all()
    return render(request,'student.html',{'student':students})

def get_student_by_id(request,id):
       student=Student.objects.get(pk=id)
       return render(request,'mystudent.html',{'student':student})

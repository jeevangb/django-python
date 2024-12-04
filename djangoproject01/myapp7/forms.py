from django import forms
from myapp7.models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= '__all__'
        # fields=['name','address']
        labels = {'name':'enter name', 'age':'Enter your age'}
        error_messages={'name':{'required':'Please enter your name'}}
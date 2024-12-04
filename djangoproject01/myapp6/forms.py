from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=30)
    mail = forms.CharField(max_length=30)
    age = forms.IntegerField()
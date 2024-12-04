from django import forms
from django.core import validators

#custom validation
def start_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError("Please enter a valid string")

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100,validators=[start_with_s])
    address = forms.CharField(validators=[validators.MaxLengthValidator(8)])#built in validation
    mail = forms.EmailField(max_length=30)
    age = forms.IntegerField()
    password = forms.CharField()
    retype_password = forms.CharField()

#multiple field validation
    def clean(self):
        super().clean()
        pwd=self.cleaned_data['password']
        rpwd=self.cleaned_data['retype_password']
        if pwd != rpwd:
            raise forms.ValidationError('Passwords do not match')


#specific field validation
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)<6:
            raise forms.ValidationError('Name must be at least 6 characters')
        return name

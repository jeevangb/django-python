from django.contrib import admin

from myapp2.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','mail','age']

# admin.site.register(Employee, EmployeeAdmin)
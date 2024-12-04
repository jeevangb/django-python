from django.contrib import admin

from myapp4.models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','mail','age']

# Register your models here.
# admin.site.register(Student,StudentAdmin)
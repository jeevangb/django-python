from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    mail= models.CharField(max_length=30)
    age=models.IntegerField()

    # def __str__(self):
    #     return str(self.name)


class Student(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    mail= models.CharField(max_length=30)
    age=models.IntegerField()

    class Meta:
        db_table = 'student_details'
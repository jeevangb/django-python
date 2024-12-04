from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    age = models.IntegerField()

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('V1/',views.v1),
    path('V2/',views.v2),
]

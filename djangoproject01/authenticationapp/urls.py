from django.urls import path
from authenticationapp import views

urlpatterns=[
    path('',views.sign_up),
]
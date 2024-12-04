from django.urls import path
from myapp8 import views

urlpatterns=[
    path('',views.home,name='myhome'),
    path('emp/',views.emp_details,name='display'),

]
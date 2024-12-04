from django.urls import path
from myapp2 import views

urlpatterns=[
    path('/myview',views.my_view),
    path('/empdet',views.emp_details),
    path('/v1',views.v1),
    path('',views.v2),
]
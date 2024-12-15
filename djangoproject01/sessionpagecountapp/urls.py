from django.urls import path
from sessionpagecountapp import views

urlpatterns=[
    path('',views.page_count_view),
]
from django.urls import path
from myapp4 import views

urlpatterns=[
    path('stuall/',views.student_view),
    path('stu/<int:id>',views.get_student_by_id),
]
from django.urls import path

from cookieapp1 import views

urlpatterns=[
    path('set/',views.set_cookies),
    path('get/',views.get_cookies),
    path('del/',views.del_cookies)
]

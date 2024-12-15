"""
URL configuration for djangoproject01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include('myapp.urls')),
    path('myapp1/',include('myapp1.urls')),
    path('myapp2/',include('myapp2.urls')),
    path('myapp3/',include('myapp3.urls')),
    path('myapp4/',include('myapp4.urls')),
    path('myapp5/',include('myapp5.urls')),
    path('myapp6/',include('myapp6.urls')),
    path('myapp7/',include('myapp7.urls')),
    path('myapp8/',include('myapp8.urls')),
    path('cookieapp/',include('cookieapp.urls')),
    path('cookieapp1',include('cookieapp1.urls')),
    path('cookiepagecountapp',include('cookiepagecountapp.urls')),
    path('sessionapp',include('sessionapp.urls')),
    path('testcookieapp',include('testcookieapp.urls')),
    path('',include('sessionpagecountapp.urls')),
]

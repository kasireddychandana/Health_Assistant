"""
URL configuration for Health_assistant project.

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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('infectious/',include('website.urls')),
    path('deficiency/',include('website.urls')),
    path('genetic/',include('website.urls')),
    path('mental/',include('website.urls')),
    path('neurological/',include('website.urls')),
    path('noncommunicable/',include('website.urls')),
    path('predeficiency/',include('website.urls')),
    path('preinfectious/',include('website.urls')),
    path('pregenetic/',include('website.urls')),
    path('premental/',include('website.urls')),
    path('preneurological/',include('website.urls')),
    path('prenoncommunicable/',include('website.urls')),
    path('predictions/', include('website.urls')),
    path('streamlit/', include('website.urls')),
    path('contact/', include('website.urls')),

    


]

"""Mymood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from Mymood.controler import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mood),
    # path('sign_in/', sign_in),
    path('sign_in/', query_happiness),
    path('redirect_sign_up/', redirect_sign_up),
    path('sign_up/', sign_up),
    path('select_emoji/', select_emoji),
    path('submit_emoji/', submit_emoji),
    path('query_happiness/', query_happiness)
]
# urlpatterns += staticfiles_urlpatterns()

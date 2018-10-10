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

from django.contrib import admin
from django.urls import path
from Mymood.controler import *
from django.conf.urls import include, url

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/$', admin.site.urls, name='admin'),
    url(r'^$', mood),
    # path('sign_in/', sign_in),
    url(r'^sign_in/$', query_happiness),
    url(r'^redirect_sign_up/$', redirect_sign_up),
    url(r'^sign_up/$', sign_up),
    url(r'^select_emoji/(.+)/$', select_emoji, name='select_emoji'),
    url(r'^submit_emoji/$', submit_emoji, name='submit_emoji'),
    url(r'^query_happiness/$', query_happiness),
    # path('query_happiness/', include('models_app.urls'))
    # url(r'^ajax_list/$', 'tools.views.ajax_list', name='ajax-list'),
    # url(r'^ajax_dict/$', 'tools.views.ajax_dict', name='ajax-dict'),
]
# urlpatterns += staticfiles_urlpatterns()

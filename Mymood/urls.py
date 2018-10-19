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
    # url(r'^admin/$', admin.site.urls, name='admin'),
    # url(r'^$', mood),
    # url(r'^sign_in/$', query_happiness),
    # url(r'^redirect_sign_up/$', redirect_sign_up),
    # url(r'^sign_up/$', sign_up),
    # url(r'^select_emoji/(.+)/$', select_emoji, name='select_emoji'),
    # url(r'^submit_emoji/$', submit_emoji, name='submit_emoji'),
    # url(r'^query_happiness/$', query_happiness),

    path('admin/', admin.site.urls),
    path('', mood),
    path('sign_in/', sign_in),
    path('redirect_sign_up/', redirect_sign_up),
    path('sign_up/', sign_up),
    path('select_emoji/<int:user_id>/', select_emoji),
    path('submit_emoji/', submit_emoji),
    path('register_messenger/<int:user_id>/', register_messenger),
    path('submit_register/', submit_register),
    path('query_happiness/', query_happiness),
    path('refresh_happiness/', refresh_happiness),
    path('export_csv/', export_csv),
    path('jump_members_in_teams/', jump_members_in_teams),
    path('query_members_in_teams/', query_members_in_teams),
    path('switch_members/', switch_members),
    path('create_teams/', create_teams),
    path('check_team_name/', check_team_name),
    path('jump_events/', jump_events),
    path('save_event/', save_event),
    path('query_events/', query_events),
    path('query_teams/', query_teams),
    path('get_webhook/<int:psid>/', get_webhook),
    path('save_happiness_level/<happiness_level>', save_happiness_level)
    # path('query_happiness/', include('models_app.urls'))
]
# urlpatterns += staticfiles_urlpatterns()

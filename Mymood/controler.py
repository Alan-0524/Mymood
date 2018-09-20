from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
import time


def mood(request):
    base_url = request.get_raw_uri()
    request.session['base_url'] = base_url
    return render(request, 'response/pages-sign-in.html')


def sign_in(request):
    return render(request, 'response/index.html')


def redirect_sign_up(request):
    return render(request, 'response/pages-sign-up.html')


def sign_up(request):
    email = request.POST.get("email")
    password = make_password(request.POST.get("password"))
    print(email, password)
    return render(request, 'response/index.html')

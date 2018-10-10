from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Mymood.biz import process_happiness


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


@xframe_options_exempt
def select_emoji(request):
    base_url = request.get_host()
    request.session['base_url'] = base_url
    # context = {
    #     'user_id': user_id,
    # }
    return render(request, 'response/select-emoji.html')


@xframe_options_exempt
@csrf_exempt
def submit_emoji(request):
    data = request.POST
    own = data.get('own')
    team = data.get('team')
    user_id = data.get('user_id')
    process_happiness.save_happiness(own, team, user_id)
    ret = {"status": 0, 'url': ''}
    return JsonResponse(ret)


def query_happiness(request):
    happiness_list = process_happiness.query_happiness()
    context = {
        'happiness_list': happiness_list,
    }
    return render(request, 'response/charts-chartjs.html', context)

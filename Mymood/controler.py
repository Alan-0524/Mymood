from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Mymood.biz import process_happiness, process_teams, process_members, process_events
from django.utils.timezone import now, timedelta
import csv
from django.views.decorators.http import require_http_methods


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


@require_http_methods(["GET"])
def get_webhook(request, psid):
    result = process_members.query_member(psid)
    if result is True:
        data = {
            'status': '1',
        }
    elif result is False:
        data = {
            'status': '0',
        }
    else:
        data = {
            'status': '9',
        }
    return JsonResponse(data, safe=False)


@xframe_options_exempt
def select_emoji(request, user_id):
    base_url = request.get_host()
    request.session['base_url'] = base_url
    context = {
        'user_id': user_id,
    }
    return render(request, 'response/select-emoji.html', context)


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


@xframe_options_exempt
def register_messenger(request, user_id):
    base_url = request.get_host()
    request.session['base_url'] = base_url
    context = {
        'user_id': user_id,
    }
    return render(request, 'response/register_messenger.html', context)


@xframe_options_exempt
@csrf_exempt
def submit_register(request):
    data = request.POST
    user_name = data.get('user_name')
    email = data.get('email')
    user_id = data.get('user_id')
    process_members.save_members(user_id, user_name, email)
    ret = {"status": 0}
    return JsonResponse(ret)


def query_happiness(request):
    happiness_list_teams = process_happiness.query_all_happiness(request, 'team_hpns')
    happiness_list_individuals = process_happiness.query_all_happiness(request, 'idvl_hpns')
    team_list = process_teams.query_all_teams(request)
    start_date = now().date() + timedelta(days=-30)  # before 30 days
    end_date = now().date()
    context = {'happiness_list_teams': happiness_list_teams, 'happiness_list_individuals': happiness_list_individuals,
               'team_list': team_list, 'start_date': start_date, 'end_date': end_date}
    return render(request, 'response/charts-c3.html', context)


@csrf_exempt
def refresh_happiness(request):
    happiness_list_teams = process_happiness.query_all_happiness(request, 'team_hpns')
    happiness_list_individuals = process_happiness.query_all_happiness(request, 'idvl_hpns')
    context = {'happiness_list_teams': happiness_list_teams, 'happiness_list_individuals': happiness_list_individuals}
    return JsonResponse(context)


@csrf_exempt
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="happiness.csv"'
    writer = csv.writer(response)

    happiness_list_teams = process_happiness.query_all_happiness(request, 'team_hpns')
    happiness_list_individuals = process_happiness.query_all_happiness(request, 'idvl_hpns')

    writer.writerow(['For teams'])
    for i in range(0, len(happiness_list_teams)):
        happiness_data_teams = happiness_list_teams[i]
        writer.writerow(happiness_data_teams)
    writer.writerow([''])
    writer.writerow([''])
    writer.writerow(['For owns'])
    for j in range(0, len(happiness_list_individuals)):
        happiness_data_teams = happiness_list_individuals[j]
        writer.writerow(happiness_data_teams)
    return response


@csrf_exempt
def switch_members(request):
    result = process_members.switch_members(request)
    if result == "success":
        ret = {"status": 0}
    else:
        ret = {"status": 1}
    return JsonResponse(ret)


def jump_members_in_teams(request):
    team_list = process_teams.query_all_teams(request)
    context = {'team_list': team_list}
    return render(request, 'response/members-table.html', context)


@csrf_exempt
def query_members_in_teams(request):
    html_text = process_members.query_members_in_teams(request)
    context = {
        'html_text': html_text,
    }
    return JsonResponse(context)


@csrf_exempt
def check_team_name(request):
    result = process_teams.check_team_name(request)
    if result is True:
        ret = {"status": 1}
    if result is False:
        ret = {"status": 0}
    return JsonResponse(ret)


@csrf_exempt
def create_teams(request):
    result = process_teams.create_teams(request)
    if result == "success":
        ret = {"status": 0}
    else:
        ret = {"status": 1}
    return JsonResponse(ret)


def jump_events(request):
    context = {'event_list': 'event_list'}
    return render(request, 'response/events-table.html', context)


@csrf_exempt
def query_events(request):
    html_text = process_events.query_events()
    context = {
        'html_text': html_text,
    }
    return JsonResponse(context)


@csrf_exempt
def save_event(request):
    result = process_events.save_event(request)
    if result == "success":
        ret = {"status": 0}
    else:
        ret = {"status": 1}
    return JsonResponse(ret)


@csrf_exempt
def query_teams(request):
    html_text = process_teams.query_teams_html(request)
    context = {
        'html_text': html_text,
    }
    return JsonResponse(context)

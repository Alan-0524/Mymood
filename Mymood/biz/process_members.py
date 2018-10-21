from models_app.models import *
import html
import uuid
from Mymood import messenger_utility
from django.contrib.auth.hashers import make_password
import random
import datetime, time


def switch_members(request):
    try:
        user_id = request.POST.get("user_id")
        team_id = request.POST.get("team_id")
        user = TblUser.objects.get(user_id=user_id)
        origin_team_id = user.team_id
        user.team_id = team_id
        user.save()
        if team_id == "99999":
            assign_time(origin_team_id)
        else:
            assign_time(team_id)
            assign_time(origin_team_id)
    except Exception as e:
        print("Error info:----------------", e)
        return "error"
    return "success"


def assign_time(team_id):
    if team_id != "99999":
        team = TblTeam.objects.get(team_id=team_id)
        start = int(team.wt_start)
        end = int(team.wt_end)
        difference = end - start
        list_user = TblUser.objects.filter(team_id=team_id)
        total = len(list_user)
        format = "%H:%M:%S"
        start = str(start)+":00:00"
        if total > 0:
            interval = difference / total * 0.5 * 3600
            for i in range(0, total):
                user = list_user.__getitem__(i)
                first_time = datetime.datetime(*time.strptime(start, format)[:6]) + datetime.timedelta(
                    seconds=interval * i)
                ft = first_time.strftime(format)
                user.first_time = ft
                second_time = datetime.datetime(*time.strptime(ft, format)[:6]) + datetime.timedelta(
                    seconds=total * interval)
                st = second_time.strftime(format)
                user.second_time = st
                user.save()


def query_members_in_teams(request):
    list_query_teams = TblTeam.objects.all()
    text = str("")
    for i in range(0, len(list_query_teams)):
        team = list_query_teams.__getitem__(i)  # Get all objects
        text = text + "<thead><tr><th>#</th><th></th><th>" + team.name + "</th><th>first start time</th><th>second start time</th></tr></thead><tbody>"

        list_query_members = TblUser.objects.filter(team_id=team.team_id)
        for j in range(0, len(list_query_members)):
            member = list_query_members.__getitem__(j)
            text = text + "<tr><td>" + str(
                j + 1) + "</td><td width='20px'><input class='icheck' onclick=""switch_team('" + member.user_id + "','" + member.user_name + "')"" type='radio' name='rad1'></td><td>" + member.user_name + "</td><td>" + member.first_time + "</td><td>" + member.second_time + "</td></tr>"
        text = text + "</tbody>"
    html_text = html.unescape(text)
    return html_text


def query_member(psid):
    user_list = TblUser.objects.filter(user_id=str(psid))
    if len(user_list) > 0:
        return True
    else:
        messenger_utility.push_register(str(psid))
        return False


def create_members(user_id, user_name, email):
    try:
        if check_user_id(user_id) == "1":
            return "User already exists"
        elif check_user_name(user_name) == "1":
            return "Username already exists"
        else:
            user = TblUser()
            user.id = str(uuid.uuid1()).replace("-", "")
            user.user_id = user_id
            user.user_name = user_name
            user.email = email
            user.first_time = "00:00"
            user.first_time_status = 0
            user.second_time = "00:00"
            user.second_time_status = 0
            user.role = 2
            user.team_id = "99999"
            user.save()
            messenger_utility.push_success(str(user_id))
            return "success"
    except Exception as e:
        print("Error info:----------------", e)
        return "error"


def create_researcher(request):
    user_name = request.POST.get("user_name")
    if check_user_name(user_name) == "1":
        return "exists"
    else:
        user = TblUser()
        u_id = ''.join(str(random.choice(range(10))) for _ in range(16))
        user.id = str(uuid.uuid1()).replace("-", "")
        user.user_id = u_id
        user.user_name = user_name
        user.role = 1
        password = make_password(request.POST.get("password"))
        user.password = password
        user.save()
        return "success"


def check_user_name(user_name):
    user = TblUser.objects.filter(user_name=user_name)
    if len(user) > 0:
        return "1"
    else:
        return "0"


def check_user_id(user_id):
    user = TblUser.objects.filter(user_id=user_id)
    if len(user) > 0:
        return "1"
    else:
        return "0"

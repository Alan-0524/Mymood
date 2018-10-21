from models_app.models import *
import uuid
from django.db.models import Max
import random
import html
from django.db.models import Q
from Mymood.biz import process_members


def query_all_teams(request):
    team_list = TblTeam.objects.all()
    return team_list


def create_teams(request):
    try:

        name = request.POST.get("name")
        team_size = request.POST.get("team_size")
        wt_start = request.POST.get("wt_start")
        wt_end = request.POST.get("wt_end")
        week_push = request.POST.get("week_push")
        id = request.POST.get("id")
        if id != "" and id is not None:
            team = TblTeam.objects.get(id=id)
        else:
            team = TblTeam()
            team.id = str(uuid.uuid1()).replace("-", "")
            new_id = random.randint(0, 99999)
            check_team_id = TblTeam.objects.filter(team_id=new_id)
            if check_team_id.exists():
                new_id = random.randint(0, 99999)
            else:
                team.team_id = new_id
            if check_team_name_2(name) == "1":
                return "Team name already exists"
        team.name = name
        team.team_size = int(team_size)
        if len(wt_start) == 1:
            wt_start = "0" + wt_start
        team.wt_start = str(wt_start)
        if len(wt_end) == 1:
            wt_end = "0" + wt_end
        team.wt_end = wt_end
        team.week_push = week_push
        team.save()
        process_members.assign_time(team.team_id)
    except Exception as e:
        print("Error info:----------------", e)
        return "System maintenance, please try again later"
    return "success"


def get_team(request):
    try:
        id = request.POST.get("id")
        team = TblTeam.objects.get(id=id)
        data = {"name": team.name, "team_size": team.team_size, "wt_start": team.wt_start, "wt_end": team.wt_end,
                "week_push": team.week_push}
        return data
    except Exception as e:
        return "error"


def delete_team(request):
    try:
        id = request.POST.get("id")
        team = TblTeam.objects.get(id=id)
        users = TblUser.objects.filter(team_id=team.team_id)
        if len(users) != 0:
            return "There are members in this group, you cannot delete this group."
        else:
            team.delete()
            return "success"
    except Exception as e:
        return "error"


def check_team_name_2(name):
    team = TblTeam.objects.filter(name=name)
    if len(team) > 0:
        return "1"
    else:
        return "0"


def check_team_name(request):
    team_name = request.POST.get("team_name")
    team = TblTeam.objects.filter(name=team_name)
    if team.exists():
        return True
    else:
        return False


def query_teams_html(request):
    list_query_teams = TblTeam.objects.all()
    text = str("")
    for i in range(0, len(list_query_teams)):
        team = list_query_teams.__getitem__(i)
        text = text + "<option value='" + team.team_id + "'>" + team.name + "</option>"
    html_text = html.unescape(text)
    return html_text


def load_teams(request):
    text = str("")
    team_list = TblTeam.objects.filter(~Q(team_id='99999'))
    for i in range(0, len(team_list)):
        team = team_list.__getitem__(i)
        id = team.id
        name = team.name
        start = team.wt_start
        end = team.wt_end
        size = team.team_size
        week_push = team.week_push
        number_members = len(TblUser.objects.filter(team_id=team.team_id))
        week = ""
        if week_push.find("0") != -1:
            week = week + "Monday,"
        if week_push.find("1") != -1:
            week = week + "Tuesday,"
        if week_push.find("2") != -1:
            week = week + "Wednesday,"
        if week_push.find("3") != -1:
            week = week + "Thursday,"
        if week_push.find("4") != -1:
            week = week + "Friday,"
        if week_push.find("5") != -1:
            week = week + "Saturday,"
        if week_push.find("6") != -1:
            week = week + "Sunday,"

        text = text + "<tr><td><a href='javascript:void(0)'><i class='fa fa-edit' onclick=""edit_team('" + id + "')""></i></a></td><td><a href='javascript:void(0)'><i class='fa fa-minus-square-o' onclick=""delete_team('" + id + "')""></i></a></td><td>" + name + "</td><td>" + str(
            number_members) + "</td><td>" + week + "</td><td>" + start + ":00</td><td>" + end + ":00</td></tr>"
    html_text = html.unescape(text)
    return html_text

from models_app.models import *
import uuid
from django.db.models import Max
import random
import html


def query_all_teams(request):
    team_list = TblTeam.objects.all()
    return team_list


def create_teams(request):
    try:
        team_name = request.POST.get("team_name")
        team = TblTeam()
        team.id = str(uuid.uuid1()).replace("-", "")
        new_id = random.randint(0, 99999)
        check_team_id = TblTeam.objects.filter(team_id=new_id)
        if check_team_id.exists():
            new_id = random.randint(0, 99999)
        else:
            team.team_id = new_id
        team.name = team_name
        team.save()
    except Exception as e:
        print("Error info:----------------", e)
        return "error"
    return "success"


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

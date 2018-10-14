from models_app.models import *
import html
import uuid
from Mymood import messenger_utility

def switch_members(request):
    try:
        user_id = request.POST.get("user_id")
        team_id = request.POST.get("team_id")
        user = TblUser.objects.get(user_id=user_id)
        user.team_id = team_id
        user.save()
    except Exception as e:
        print("Error info:----------------", e)
        return "error"
    return "success"


def query_members_in_teams(request):
    list_query_teams = TblTeam.objects.all()
    text = str("")
    for i in range(0, len(list_query_teams)):
        team = list_query_teams.__getitem__(i)
        text = text + "<thead><tr><th>#</th><th>" + team.name + "</th></tr></thead><tbody>"

        list_query_members = TblUser.objects.filter(team_id=team.team_id)
        for j in range(0, len(list_query_members)):
            member = list_query_members.__getitem__(j)
            text = text + "<tr onclick=""switch_team('" + member.user_id + "','" + member.user_name + "')""><td>" + str(
                j + 1) + "</td><td>" + member.user_name + "</td></tr>"
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


def save_members(user_id, user_name, email):
    try:
        user = TblUser()
        user.id = str(uuid.uuid1()).replace("-", "")
        user.user_id = user_id
        user.user_name = user_name
        user.email = email
        user.role = 0
        user.team_id = "99999"
        user.save()
    except Exception as e:
        print("Error info:----------------", e)

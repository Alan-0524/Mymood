from models_app.models import *
imp

def query_teams_html(request):
    list_query_teams = TblTeam.objects.all()
    text = str("")
    for i in range(0, len(list_query_teams)):
        team = list_query_teams.__getitem__(i)
        text = text + "<option value='" + team.team_id + "'>" + team.name + "</option>"
    html_text = html.unescape(text)
    return html_text

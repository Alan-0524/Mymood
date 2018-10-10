from models_app.models import *
import uuid
import time


def query_happiness():
    happiness_list = TblHappiness.objects.all()
    return happiness_list


def save_happiness(own, team, user_id):
    try:
        user = TblUser.objects.get(pk=user_id)
        team_id = user.team_id
        happiness = TblHappiness()
        happiness.id = str(uuid.uuid1()).replace("-", "")
        happiness.team_id = team_id
        happiness.idvl_hpns = own
        happiness.team_hpns = team
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        happiness.date = time_now
        happiness.save()
    except Exception as e:
        print(e)

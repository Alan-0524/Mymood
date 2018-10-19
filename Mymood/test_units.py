from datetime import datetime, date,timedelta
from models_app.models import *
from Mymood import messenger_utility
import schedule
import time
def inc(x):
    return x + 1


def test_answer():
    assert inc(5) == 6


# print(str(datetime.now().time())>'15:33:47')



# def test_job():
#     # 01236
#     day = str(datetime.now().weekday())
#     team_list = TblTeam.objects.filter(team_id="00001")
#     for i in range(0, len(team_list)):
#         team = team_list.__getitem__(i)
#         week_push = team.week_push
#         team_id = team.team_id
#         result = day in week_push
#         if result is True:
#             user_list = TblUser.objects.filter(team_id=team_id, role=2)
#             for j in range(0, len(user_list)):
#                 user = user_list.__getitem__(i)
#                 user_id = user.user_id
#                 first_time = user.first_time
#                 first_time_status = user.first_time_status
#                 second_time = user.second_time
#                 second_time_status = user.second_time_status
#                 now = datetime.now().time()
#                 if second_time > str(now) > first_time and first_time_status == 0:
#                     messenger_utility.push_notifications(user_id)
#                 if str(now) > second_time and second_time_status == 0:
#                     messenger_utility.push_notifications(user_id)




from django.core.management.base import BaseCommand, CommandError
from datetime import datetime, date, timedelta
from Mymood import messenger_utility
import schedule
import time
from models_app.models import *
from django.db.models import Q


# messenger_utility.push_notifications("2334765856551775")
class Command(BaseCommand):
    def handle(self, *args, **options):
        def push_notification():
            print("1")
            day = str(datetime.now().weekday())
            team_list = TblTeam.objects.filter(~Q(team_id='99999'))
            # team_list = TblTeam.objects.filter(team_id="00001")
            print("2")
            for i in range(0, len(team_list)):  # 0123456
                print("3")
                team = team_list.__getitem__(i)
                week_push = team.week_push
                team_id = team.team_id
                result = day in week_push
                if result is True:
                    user_list = TblUser.objects.filter(team_id=team_id, role=2)
                    if len(user_list) > 0:
                        for j in range(0, len(user_list)):
                            user = user_list.__getitem__(j)
                            user_name = user.user_name
                            user_id = user.user_id
                            print("user_id:" + user_id, "----user_name:", user_name, "-----team_id:", user.team_id)
                            first_time = user.first_time
                            first_time_status = user.first_time_status
                            second_time = user.second_time
                            second_time_status = user.second_time_status
                            now = datetime.now().time()
                            print(second_time, "------------", str(now), "--------", first_time)
                            if second_time > str(now) > first_time and first_time_status == 0:
                                messenger_utility.push_notifications(user_id)
                                print("4")
                            if "22:00 " > str(now) > second_time and second_time_status == 0:
                                print("5")
                                messenger_utility.push_notifications(user_id)

        schedule.every(4).seconds.do(push_notification)
        # schedule.every(10).seconds.do(job)
        # schedule.every().hour.do(job)
        # schedule.every().day.at("22:03").do(job)
        # schedule.every(5).to(10).days.do(job)
        # schedule.every().do(job)
        # schedule.every().wednesday.at("13:15").do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)

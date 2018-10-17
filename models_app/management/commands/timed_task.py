from django.core.management.base import BaseCommand, CommandError
from Mymood import messenger_utility
import schedule
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        def job():
            print("I'm working...")
            messenger_utility.push_notifications("2334765856551775")

        # schedule.every(1).seconds.do(job)
        schedule.every(10).seconds.do(job)
        # schedule.every().hour.do(job)
        # schedule.every().day.at("22:03").do(job)
        # schedule.every(5).to(10).days.do(job)
        # schedule.every().do(job)
        # schedule.every().wednesday.at("13:15").do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)

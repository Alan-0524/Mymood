import schedule
import time


def job():
    print("I'm working...")


schedule.every(10).seconds.do(job)
# schedule.every(5).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("22:03").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

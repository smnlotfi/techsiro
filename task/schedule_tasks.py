# Tasks for time
import schedule
import time
from datetime import datetime


def task_for_14():
    # Replace this with your task logic
    print("Task executed at", datetime.now())


def task_for_every_20_minutes():
    # Replace this with your task logic
    print("This job runs every 20 minutes.")


# Schedule the task to run every day at 14:00 (2:00 PM)
schedule.every().day.at("14:00").do(task_for_14)

# Schedule the task to run every 20 minutes
schedule.every(20).minutes.do(task_for_every_20_minutes)


def run_schedule():
    print(datetime.now())
    while True:
        schedule.run_pending()
        time.sleep(1)

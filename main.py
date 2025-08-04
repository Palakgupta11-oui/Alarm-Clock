import datetime
import time
import os
from playsound import playsound  # Install this with: pip install playsound

def set_alarm():
    alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")
    try:
        alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(":"))
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return

    print(f"Alarm set for {alarm_time}. Waiting...")

    while True:
        now = datetime.datetime.now()
        if (now.hour == alarm_hour and
            now.minute == alarm_minute and
            now.second == alarm_second):
            print("⏰ Wake up! Alarm time reached!")
            try:
                playsound("alarm.mp3")  # Replace with your own sound file
            except:
                print("Couldn't play the sound. Make sure 'alarm.mp3' exists.")
            break
        time.sleep(1)

if __name__ == "__main__":
    set_alarm()


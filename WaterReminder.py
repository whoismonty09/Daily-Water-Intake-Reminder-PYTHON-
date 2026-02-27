import time
import winsound

print("Water Reminder developed by Monty")
interval = int(input("Enter reminder interval in minutes: "))

print("Water Reminder Started Press Ctrl C to stop")

while True:
    time.sleep(interval * 60)
    print("Time to drink water Stay hydrated")
    winsound.Beep(1000, 1000)




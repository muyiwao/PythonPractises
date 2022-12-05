# 1 Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)

# 2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)

# 3 Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# 4 Calculate the time difference between now and new year.
from datetime import date

today = date(year=2022, month=11, day=27)
new_year = date(year=2023, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

# 5 Calculate the time difference between 1 January 1970 and now.
today = date(year=2022, month=11, day=27)
old_year = date(year=1970, month=1, day=1)
time_diff = today - old_year
print('Time diff: ', time_diff)

"""
Output:
2022-12-05 21:06:15.230857
5 12 2022 21 6
timestamp 1670274375.230857
12/05/2022, 21:06:15
date_string = 5 December, 2019
date_object = 2019-12-05 00:00:00
Time left for new year:  35 days, 0:00:00
Time diff:  19323 days, 0:00:00

Process finished with exit code 0
"""

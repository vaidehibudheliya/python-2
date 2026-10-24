from datetime import datetime as dt

date = dt.now()
print(date)
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
today = week[date.weekday()] + " " + str(date.day) + "/" + str(date.month) + "/" + str(date.year)
print ("today is",today)
time = str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
print(time)
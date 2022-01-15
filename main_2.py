import calendar
import time
import files.read as r
import datetime
c = calendar.TextCalendar (calendar.MONDAY) 
str = c.formatmonth (2022,1)
print(str)

time.sleep(5)
print("Привет")

a = datetime.datetime.today()
print("Сегодня у нас: ")
print(a)
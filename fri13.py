#Erik Hansen
#10/2/2017
#fri13.py
from calendar import weekday
from datetime import date

day = date.today().day
month = date.today().month
year = date.today().year
friday13=0

if day>13 and month!=12:
    month = month + 1

while friday13<=10:
    if weekday(year,month,13) == 4:
        friday13 += 1
        print(str(month) + '/' + '13/' + str(year))
    if month!=12:
        month += 1
    else:
        month = 1
        year +=1

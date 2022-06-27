# Example file for working with Calenders


# TODO: import the calender module
import  calendar


# TODO: create a plain text calender
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2022,1,0,0)
print(str)

# TODO: create an HTML formatted calender
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2022,1)
print(str)

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2022,8):
    print(i)

# TODO: The Calender module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated form
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# TODO: Calculate days based on a rule : For example, consider
# a team meeting on tghe first Friday of every month.
#  To figure out what days that would be for each month,
# we cam use this script:

print("team meetings will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2022,m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else: 
        meetday = weektwo[calendar.FRIDAY]
    
    print(calendar.month_name[m],meetday)

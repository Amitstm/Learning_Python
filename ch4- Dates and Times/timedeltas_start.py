# 
# Example file for working with timedelta objects
# 
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta



# TODO: construct a basic timedelta and print it

print(timedelta(days=365, hours=5, minutes=1))

# TODO: print today's date

now = datetime.now()
print('Today is', now)

# TODO: print today's date one year from now
print("One year from now it will be ", str(now + timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print('IN two  weeks and 3 days it will be', str(now + timedelta(weeks=2, days=3)) )


# Todo: calculate the date 1 week ago, formatted as a string

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d %Y")
print("One week ago it was",s)


# How many days until April Fool's Day?
today = date.today()
afd = date(today.year, 4, 1)


# TODO: use date comparison to see if April Fool's has already gone for this year
# If it has , use the replace() funcion to get the date for next year

if afd<today:
    print("Aprils Fool's Day already went by: ", ((today-afd).days))
    afd = afd.replace(year = today.year + 1)

# TODO: Now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print("it is", time_to_afd, " days until the next April Fool's Day!")
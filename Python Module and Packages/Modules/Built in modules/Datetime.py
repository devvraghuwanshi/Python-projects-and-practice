# datetime module - lets us work with date , time , timestamps , duration and timezones

# importing datetime
from datetime import date , time , datetime , timezone , timedelta

# date class : only stores date
today = date.today()
print(today)

# Creating custom date and accessing its components.
mydate = date(2005,2,7)
print(mydate)

print(mydate.month)
print(mydate.day)
print(mydate.year)

# time class - only stores time
t = time(20,40,40)
print(t)

# Accessing components of time class
print(t.hour)
print(t.minute)
print(t.second)

# datetime class - stores both date and time

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# custom datetime
dt = datetime(2026,2,7,15,18,20)
print(dt)

print(date.today())              #current date
print(datetime.now().time())     #current time
print(datetime.now())            #current datetime
print(datetime.now(timezone.utc))#utc time


# Formatting dates - strftime(string format time)
now2 = datetime.now()
print(now2.strftime("%d/%m/%Y"))

# converting string into datetime
text = "15-07-2026"
d = datetime.strptime(text,"%d-%m-%Y")

# timedelta() - used for addition adn subtraction of time
tommorow = today + timedelta(days = 1)
print(tommorow)

# difference between dates -
d1 = date(2026,7,16)
d2 = date(2005,2,7)
difference = d1 - d2
print(difference)

# comparing dates -
print(d1>d2)
print(d2<d1)
print(d1==d2)

# replace parts -
new = now.replace(year=2030)
print(new)

# weekday() - gives number of weekday
print(today.weekday())

# timestamp() - converts datetime to unix timestamp
print(now.timestamp())

# fromtimestamp() - converts timestamp to datetime
print(datetime.fromtimestamp(1784225864.107118))
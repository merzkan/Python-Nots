#Datatime module


#import datetime
from datetime import datetime

#print(dir(datetime))
#['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo'

#from datetime import datetime
#from datetime import date
#from datetime import date

#print(dir(datetime))
#['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__replace__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']

result = datetime.now()
#2024-12-23 16:53:19.943643
result1 = datetime.now().year
#2024
result2 = datetime.now().month
#12
result3 = datetime.now().day
#23
result4 = datetime.now().hour 
#16
result5 = datetime.now().minute  
#53
result6 = datetime.now().second
#19
result7 = datetime.today()
#2024-12-23 16:53:19.943668
result8 = datetime.ctime(datetime.now())
#Mon Dec 23 16:53:19 2024
result9 = datetime.strftime(datetime.now(),"%Y")
#2024
result10 = datetime.strftime(datetime.now(),"%X")
#16:53:19
result11 = datetime.strftime(datetime.now(),"%d")
#23
result12 = datetime.strftime(datetime.now(),"%A")
#Monday
result13 = datetime.strftime(datetime.now(),"%B")
#December
result14 = datetime.strftime(datetime.now(),"%Y %B %A")
#2024 December Monday

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)
print(result13)
print(result14)


print("********************************")

t = '21 Nisan 2019'
gun, ay, yil = t.split()
print(gun)
#21
print(ay)
#Nisan
print(yil)
##2019

print("********************************")

t1 = '15 April 2019 hour 10:12:30'
dt = datetime.strptime(t1, "%d %B %Y hour %H:%M:%S" )

print(dt)
#2019-04-15 10:12:30

print("********************************")

birthday = datetime(1983,5,9,12,30,10)
#1983-05-09 12:30:10
result15 = datetime.timestamp(birthday)#saniye cinsinden
#421320610.0
result16 = datetime.fromtimestamp(result15)#saniyeyi tekrar tarih bilgisine 
#1983-05-09 12:30:10
result17 = datetime.fromtimestamp(0)
#1970-01-01 03:00:00
result18 = datetime.now() - birthday 
#15204 days, 4:35:56.631055
result19 = result18.days
#15204
result19 = result18.seconds
#16740
result20 = result18.microseconds
#820086

print(birthday)
print(result15)
print(result16)
print(result17)
print(result18)
print(result19)
print(result20)

print("****************")
from datetime import timedelta

result21 = datetime.now() + timedelta(days=10)
#2025-01-02 17:10:55.877219
result22 = datetime.now() - timedelta(days=10)
#2024-12-13 17:11:47.343000
print(result21)
print(result22)
                                      
                                      

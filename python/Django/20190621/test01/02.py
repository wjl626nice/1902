# import t01
import datetime

now = datetime.datetime.now()
print(now)
dt = datetime.datetime(2019, 6, 21, 10, 14, 0, 0, None)
print(dt)
print(now - dt, type(now - dt))

td = datetime.timedelta(days=-1)
print(now+td, type(now+td))

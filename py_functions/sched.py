import sched
import time
from datetime import datetime, timedelta

'''
Works only on Python 3
'''


scheduler = sched.scheduler(timefunc=time.time)


def saytime():
    print(time.ctime())
    scheduler.enter(10, priority=0, action=saytime)

saytime()
try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Stopped.')
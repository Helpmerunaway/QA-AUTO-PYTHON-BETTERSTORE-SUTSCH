import datetime
import random

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow_date = tomorrow.date()
print(tomorrow_date)

from random import randrange
from datetime import timedelta


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


midnight = tomorrow.replace(
    hour=random.randint(0, 23),
    minute=random.randint(0, 59),
    second=0,
    microsecond=0)
mid = str(midnight.strftime("%H:%M"))
print(mid)

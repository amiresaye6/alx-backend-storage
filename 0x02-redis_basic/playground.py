#!/usr/bin/env python3
"""play ground for redis"""
import redis
import datetime
import random
import pprint

r = redis.Redis()

"""
today = str(datetime.datetime.today())
print(today)

visitors = {"amir", "alsayed", "abdulsamea"}

print(r.sadd(today, *visitors))

set_vals = r.smembers(today)
print(set_vals)

print(r.scard(today))
"""
"""
cards = [
     {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    }
]

vals = {f"hat:{random.getrandbits(32)}": card for card in cards}

# print(vals)
with r.pipeline() as pipe:
    for key, val in vals.items():
        pipe.hmset(key, val)

    pipe.execute()

pprint.pprint(r.hgetall('hat:2577126341'))
# print(r.keys())
"""
def fun1(fun):
    def wrapper(*args, **kwargs):
        print("startd")
        fun(*args, **kwargs)
        print("ended")
    return wrapper


@fun1 # decorator to run function fun1 each time we call the next functio "f"
def f(a):
    print(a)

f("hi")

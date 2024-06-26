#!/usr/bin/env python3
"""
docs https://realpython.com/python-redis/
"""
"""
this module contain all the notes related to my stydy of redis.
Redis >> stands for Remote Dictionary Service.
"""

"""
first the installation of redis and redis server

Install Redis on Ubuntu 18.04
FIRST INSTALL THE REDIS SERVER
$ sudo apt-get -y install redis-server

SECOND INSTALL REDIS PYTHON PACKAGE
$ pip3 install redis

THIRD CHANGE THE CONFIG TO CONNECT TO LOCAL HOST AT 127.0.0.0
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

remimber to run the server { sudo service redis-server start }

to open the redis comand line interface 
$ redis-cli

to stop redis server
$ redis-cli shutdown.
"""

"""
redis CLI  commands
RECOMMENDED CAPITAL CASE

PING >> check if ther is a coonection [returns PONG if there is a coonection]

ECHO "MASSAGE"  >> Will print MASSAGE

SET key value
SET name "amir"
SET age 22
SET STUDIENT "true"

SET server:name homeServer
SET server:ip 127.0.0.1

GET serve:ip

GET KEY
GET name >> will return "amir"
and so on 

INCR age >> will increase the age by 1 >> 23
DECR age >> will decrease the age by 1 >> 22

EXISTS KEY >> WILL RETURN 1 IF TEH KEY EXISTS AND 0 IF NOT

EXISTS amir >> 1
EXISTS AMIR >> 0

DEL amir >> will delete amir
EXISTS amir >> 0
GET amir >> nil >> nothing there

FLUSHALL >> WILL CLEAR ALL TEH KEY VALUES

SET GREETING "HELLO, WORLD"
EXPIRE GREETING 50 >> THIS WILL EXPIRE AFTER 50 SECONDS

TTL GREETING >> WILL RETURN THE TIME REMINNIG BEFORE EXPIREND 
[TTL >> TIME TO LIVE]

IF YOU WANT TO SET THE VALUE AN DEXPIREATION AT ONE COMAND

SETEX NAME 20 "AMIR"

PERSIST AMIR >> TO STOP THE EXPIRATION DATE AT ALL [NO EXPIRE DATE]

MSET >> SET MULTIBLE KEY VALUES

MSET NAME "AMIR ALSAYED" AGE 21 COND "STUDENT"

MGET >> GET MULTIBLE VALUES AT ONCE

MGET NAEE AGE COND >> WIIL GET THE NAME, THE AGE, AND THE COND LINE BY LINE

APPEND >> WILL APPEND A VALUE TO THE TO THE END OF THE EXISTING VAL

APPEND NAME " ABDULSAMEA" >> { NAME WILL BE AMIR ALSAYED ABDULSAMEA }

RENAME >> WILL CHANGE THE KEY NAME TO ANOTHER ONE

RENAME NAME FULLNAME


WORKING WITH LISTS

LPUSH >> PUSH THE NEW VALUE TO THE START OF A LIST
RPUSH >> PUSH THE NEW VALUE TO THE END OF A LIST

RPUSH NAMES "AMIR"
RPUSH NAMES "ALSAYED"
RPUSH NAMES "ABDULSAMEA"
RPUSH NAMES "MOHAMED"

LRANGE >> WILL RETURN THE LIST BASED ON THE RANGE

LRANGE NAMES 0 -1 >> WILL RETURN THE WHOAL LIST

LRANGE NAMES 1 2 >> WILL RETURN ALSAYED, ABDULSAMEA

LRANGE AMIR 0 0 >> WILL RETURN AMIR

LLEN >> RETURNS THE LENGTH OF THE LIST

LLEN NAMES >> EX: 4

LPOP >> POPS THE FIRST VALUE FROM THE LEFT
RPOP >> POPS TEH FIRST VALUE FROM THE RIGHT

LPOP NAMES >> REMOVES AMIR AND RETURNS IT
RPOP NAMES >> REMOVES MOHAMED AND RETURNS IT

LINSERT >> ADDS THE NEW VALUE BEFORE SPECIFIC VALUE

INSERT NAMES BEFORE "AMIR" "Amir"

WORKING WITH SETS

SADD >> ADDS THE VALUE TO THE SET

SADD CARS "BMW"
SADD CARS "TOYOTA"
SADD CARS "MERCEDIS"
SISMEMBER >> RETURNS 1 IF THE VALUE IS MIMEBER OF THE SES

SISMIMPER CARS "BMW" >> 1
SISMIMPER CARS "FORD" >> 0

SMEMBERS CARS >> RETURN THE SET OF CARS
SCARD >> RETURN HOW MANY ELEMNTS ON A SET
SCARD CARS >> 3

SMOVE >> MOVES A VALUE FROM ONE SET TO ANOTHER

SMOVE CARS NEW_CARS "BMW" >> WILL MOVE THE BMW FROM CARS SET TO THE NEW_CARS SET

SREM CARS "TOYOTA" >> WILL REMOVE TOYOTA FROM CARS SET

WORKING WITH SORTED SETS

ZADD USERS 2002 "AMIR ALSAYED"
ZADD USERS 2009 "EMAN ALSAYED"
ZADD USERS 2000 "AHMED ALSAYED"

ZRANK USERS "AMIR ALSAYED" >> WILL RETURN 1 BECAUSE 2009 > 2002 > 2000

ZRANGE USERS 0 -1 >> WILL PRINT ALL THE MEMBERS ON THE SORTED SET

ZINCRBY USERS 1 "AMIR ALSAYED" >> 2003
ZINCRBY USERS 10 "AMIR ALSAYED" >> 2013

WORKING WITH HASHS

HSET USER:AMIR NAME "AMIR ALSAYED"
HSET USER:AMIR EMAIL "amiralsayed.work@gmail.com"

HGET USR:AMIR NAME >> PRINTS AMIR ALSAYED
HGET USER:AMIR EMAILI >> amiralsayed.work@gmail.com
HGETALL >> WILL PRINT ALL ABOUT SERTEN USER

HGETALL USER:AMIR >> WILL PRINUT
127.0.0.1:6379> HGETALL USR:AMIR
1) "NAME"
2) "AMIR ALSAYED"
3) "AGE"
4) "22"
5) "EMAIL"
6) "amiralsayed.work@gmail.com"

HMSET >> WILL ADD MULTIBLE RECORDS TO THE HASH SET

HMSET USR:AM NAME "AMIR" AGE 22 HEIGHT 178

HKEYS USR:AM >> WILL RETURN ONLY THE KEYS
HVALS USR:AM >> WILL RETURN ONLY THE VALUES

HINCRBY USR:AM AGE 1 >> WILL INCREASE THE AGE OF TEH USER AM BY 1 >> 23

HDEL USR:AM HEIGHT >> WILL DELETE THE HEIGHT FROM USER AM

HLEN USR:AM >> WILL RETURN THE NUMBER OF KEY VAL PAIRS >> 2

HLEN USR:AMIR >> 3

HSTRLEN USR:AM NAME >> THE LENGTH OF NAME OF USR AM IS  4

AND THATS IT, THE BASICS OF REDIS :)

"""

"""important"""
"""
redis in py returns all in byte format so you may have to cast it like so:
$ r.get("Bahamas").decode("utf-8")
"""

# Quickly connecting to redis
# There are two quick ways to connect to Redis.

# Assuming you run Redis on localhost:6379 (the default)

import redis
r = redis.Redis()
r.ping()
# Running redis on foo.bar.com, port 12345

import redis
r = redis.Redis(host='foo.bar.com', port=12345)
r.ping()
# Another example with foo.bar.com, port 12345

import redis
r = redis.from_url('redis://foo.bar.com:12345')
r.ping()

# redis pipeline

import random

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
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
    })
}
# the pipeline reduces the db access times, it buffers the operations and 
# does it at one trip to the server
with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hmset(h_id, hat)
    pipe.execute() # once written, the pipline executes its operations


import logging
import redis

logging.basicConfig()

class OutOfStockError(Exception):
    """Raised when PyHats.com is all out of today's hottest hat"""

def buyitem(r: redis.Redis, itemid: int) -> None:
    with r.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                # Get available inventory, watching for changes
                # related to this itemid before the transaction
                pipe.watch(itemid)
                nleft: bytes = r.hget(itemid, "quantity")
                if nleft > b"0":
                    pipe.multi()
                    pipe.hincrby(itemid, "quantity", -1)
                    pipe.hincrby(itemid, "npurchased", 1)
                    pipe.execute()
                    break
                else:
                    # Stop watching the itemid and raise to break out
                    pipe.unwatch()
                    raise OutOfStockError(
                        f"Sorry, {itemid} is out of stock!"
                    )
            except redis.WatchError:
                # Log total num. of errors by this user to buy this item,
                # then try the same process again of WATCH/HGET/MULTI/EXEC
                error_count += 1
                logging.warning(
                    "WatchError #%d: %s; retrying",
                    error_count, itemid
                )
    return None


# decorators in py

def fun1(fun):
    def wrapper(*args, **kwargs):
        print("startd")
        fun()
        print("ended")
    return wrapper


@fun1 # decorator to run function fun1 each time we call the next functio "f"
def f(a):
    print("a")

f("hi")

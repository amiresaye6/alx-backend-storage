#!/usr/bin/env python3
"""
task: 0. Writing strings to Redis
condition: mandatory
required:
Create a Cache class. In the __init__ method, store an instance of the Redis
client as a private variable named _redis (using redis.Redis()) and flush
the instance using flushdb.

Create a store method that takes a data argument and returns a string. The
method should generate a random key (e.g. using uuid), store the input
data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be
a str, bytes, int or float.
"""
import redis
from redis import Redis
from typing import Union
from typing import Any
from uuid import uuid4


class Cache():
    """
    cashing class using redis
    """

    def __init__(self) -> None:
        """
        initial constructor for Cashe class
        """
        self._redis: Redis = redis.Redis()
        self._redis.flushall()

    def store(self, data: Any) -> str:
        """
        Store data in Redis and return the generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        id = str(uuid4())

        self._redis.set(id, data)

        return id

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
from typing import Union, Callable, Optional
from functools import wraps
from uuid import uuid4


def count_calls(method: callable) -> callable:
    """to be done"""
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ to be added """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    cashing class using redis
    """

    def __init__(self) -> None:
        """
        initial constructor for Cashe class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """getter function for class Cash"""
        result = self._redis.get(key)

        if fn:
            return fn(result)
        return result

    def get_str(self, key: str) -> str:
        """docs to be added"""
        val = self._redis.get(key)

        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """DOCS TO BE ADDED"""
        int_val = self._redis.get(key)
        try:
            int_val = int(int_val.decode("utf-8"))
            return int_val
        except Exception:
            int_val = 0
        return int_val

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
import functools
from typing import Union, Callable, Optional
from uuid import uuid4

from pprint import pprint

import redis.retry


def count_calls(method: Callable) -> Callable:
    """to be done"""
    key = method.__qualname__
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ to be added """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """to be added"""
    key = method.__qualname__
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """to be added"""
        return_val = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:inputs", str(args))
        self._redis.rpush(f"{key}:outputs", str(return_val))
        return return_val
    return wrapper


def replay(func: Callable) -> None:
    """to be added"""

    r = redis.Redis()
    key = func.__qualname__

    times_called = r.get(str(key))

    try:
        times_called = int(times_called.decode("utf-8"))
    except Exception:
        times_called = 0
    # may have failed some text cases
    # print(f"{key} was called {times_called} times:")
    print("{} was called {} times:".format(key, times_called))

    inputs = r.lrange("{}:inputs".format(key), 0, -1)
    outputs = r.lrange("{}:outputs".format(key), 0, -1)

    # for i in range(len(inputs)):
    #     input_ = inputs[i].decode("utf-8")
    #     output = outputs[i].decode("utf-8")
    #     print(f"{key}(*{input_}) -> {output}")

    # for i in inputs:
    #     pprint(i.decode("utf-8"))
    # for i in outputs:
    #     pprint(i.decode("utf-8"))

# Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8

    for input_, output in zip(inputs, outputs):
        try:
            input_ = input_.decode("utf-8")
        except Exception:
            input_ = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

    print("{}(*{}) -> {}".format(key, input_, output))


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
    @call_history
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

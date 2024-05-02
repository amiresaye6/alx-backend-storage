#!/usr/bin/env python3
"""
task: 5. Implementing an expiring web cache and tracker
condition: #advanced
required:
In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:). The core of the function is very
simple. It uses the requests module to obtain the HTML content of a particular
URL and returns it.

Start in a new file named web.py and do not reuse the code written in
exercise.py.

Inside get_page track how many times a particular URL was accessed in the key
"count:{url}" and cache the result with an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate a slow response and
test your caching.

Bonus: implement this use case with decorators.
"""


import redis
import requests
from functools import wraps
import typing
r = redis.Redis()


# def url_access_count(method):
#     """decorator for get_page function"""
#     @wraps(method)
#     def wrapper(url):
#         """wrapper function"""
#         key = "cached:" + url
#         cached_value = r.get(key)
#         if cached_value:
#             return cached_value.decode("utf-8")

#             # Get new content and update cache
#         key_count = "count:" + url
#         html_content = method(url)

#         r.incr(key_count)
#         r.set(key, html_content, ex=10)
#         r.expire(key, 10)
#         return html_content
#     return wrapper


# @url_access_count
# def get_page(url: str) -> str:
#     """obtain the HTML content of a particular"""
#     results = requests.get(url)
#     return results.text


# if __name__ == "__main__":
#     get_page('http://slowwly.robertomurray.co.uk')

def count_url_access(method: typing.Callable) -> typing.Callable:
    """wrapper function that counts access time for a url"""
    @wraps(method)
    def wrapper(url):
        """ wrapper function for count_url_access function"""

        key = "cached:" + url
        key_count = "count:{}".format(url)
# first lets look for this url in the cached values
        cached_url = r.get(key)

        if cached_url:
            return cached_url.decode("utf-8")
# url is not cached
        r.incr(key_count)
        html_response = method(url)
        r.setex(key, 10, str(html_response))

        return html_response
    return wrapper


@count_url_access
def get_page(url: str) -> str:

    result = requests.get(url)
    return result.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")

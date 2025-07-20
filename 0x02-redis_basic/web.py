#!/usr/bin/env python3
"""
Module for implementing an expiring web cache and tracker using Redis.
"""
import redis
import requests
from typing import Callable
from functools import wraps


def count_access(method: Callable) -> Callable:
    """
    Decorator to track the number of times a URL is accessed and cache the result.

    Args:
        method: The function to decorate.

    Returns:
        Callable: The wrapped function.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Increments the access count, checks the cache, and fetches the page if needed.

        Args:
            url: The URL to fetch and cache.

        Returns:
            str: The HTML content of the URL.
        """
        redis_client = redis.Redis()
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        # Increment access count
        redis_client.incr(count_key)

        # Check if URL is cached
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # Fetch content if not cached
        result = method(url)
        # Cache with 10-second expiration
        redis_client.setex(cache_key, 10, result)
        return result

    return wrapper


@count_access
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL, caches it for 10 seconds, and tracks access.

    Args:
        url: The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
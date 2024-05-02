#!/usr/bin/env python3
"""web"""
import requests
import redis
import time


def get_page(url: str) -> str:
    # Connect to Redis
    r = redis.Redis()

    # Increment access count for the URL
    r.incr(f"count:{url}")

    # Check if the page content is cached
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # Fetch the page content using requests
    response = requests.get(url)
    page_content = response.text

    # Cache the page content with an expiration time of 10 seconds
    r.setex(url, 10, page_content)

    return page_content

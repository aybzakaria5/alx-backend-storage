#!/usr/bin/env python3
"""redis"""
import redis
import uuid
from typing import Union


class Cache:
    """a class for cache"""
    def __init__(self):
        """constructure"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """dàc for store methode"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

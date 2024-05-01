#!/usr/bin/env python3
"""redis"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """docs for get methode"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
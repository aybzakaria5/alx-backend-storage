#!/usr/bin/env python3
"""updating"""


def update_topics(mongo_collection, name, topics):
    """updating"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

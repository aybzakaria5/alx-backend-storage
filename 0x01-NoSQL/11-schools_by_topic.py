#!/usr/bin/env python3
"""
finding a document in a collection
"""


def schools_by_topic(mongo_collection, topic):
    """task 11²:w
    """
    return mongo_collection.find({"topics": topic})

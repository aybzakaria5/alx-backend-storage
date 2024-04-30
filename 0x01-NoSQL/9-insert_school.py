#!/usr/bin/env python3
"""
inserting using insertone
"""


def insert_school(mongo_collection, **kwargs):
    """
    returning the id of an inserted doc by using inserted_id
    """
    return mongo_collection.insert_one(kwargs).inserted_id

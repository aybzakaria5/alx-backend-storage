#!/usr/bin/env python3
"""finding"""


def schools_by_topic(mongo_collection, topic):
    """task 11"""
    mongo_collection.find({"topic": topic})

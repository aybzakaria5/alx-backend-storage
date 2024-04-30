#!/usr/bin/env python3
"""using pythin to list documents in a collection"""


def list_all(mongo_collection):
    """lisitng all docs in a colleciton using find"""
    return list(mongo_collection.find())

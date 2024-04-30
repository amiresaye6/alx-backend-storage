#!/usr/bin/env python3
"""
task: 9. Insert a document in Python
condition: mandatory
required:
Write a Python function that inserts a new document in a collection based
on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
    mongo_collection will be the pymongo collection object
    Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs

    Args:
        mongo_collection (db colllection): the pymongo collection object
        kwargs


    Returns:
        the new _id
    """

    return mongo_collection.insert(kwargs)

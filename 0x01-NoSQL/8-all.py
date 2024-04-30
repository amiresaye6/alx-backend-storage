#!/usr/bin/env python3
"""
task: 8. List all documents in Python
condition: mandatory
required:
Write a Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
    """
    List all documents in Python.

    Args:
        mongo_collection (db colllection): the pymongo collection object

    Returns:
        an empty list if no document in the collection
    """

    if not mongo_collection:
        return []

    resp = mongo_collection.find()
    return [res for res in resp]

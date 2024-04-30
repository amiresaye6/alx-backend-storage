#!/usr/bin/env python3
"""
task: 10. Change school topics
condition: mandatory
required:
Write a Python function that changes all topics of a school document
based on the name:

    Prototype: def update_topics(mongo_collection, name, topics):
    mongo_collection will be the pymongo collection object
    name (string) will be the school name to update
    topics (list of strings) will be the list of topics approached in the
    school
"""


def update_topics(mongo_collection, name, topics):
    """
    inserts a new document in a collection based on kwargs

    Args:
        mongo_collection (db colllection): the pymongo collection object
        name (string) will be the school name to update
        topics (list of strings) will be the list of topics approached in the
        school


    Returns:
        the new _id
    """

    return mongo_collection.update_many({"name": name},
                                        {'$set': {'topics': topics}})

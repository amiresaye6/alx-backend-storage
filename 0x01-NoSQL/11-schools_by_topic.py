#!/usr/bin/env python3
"""
task: 11. Where can I learn Python?
condition: mandatory
required:
Write a Python function that returns the list of school having a specific topic

    Prototype: def schools_by_topic(mongo_collection, topic):
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    inserts a new document in a collection based on kwargs

    Args:
        mongo_collection (db colllection): the pymongo collection object
        topic (string) will be topic searched

    Returns:
        list of school having a specific topic
    """

    return mongo_collection.find({"topics": topic})

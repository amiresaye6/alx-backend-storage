#!/usr/bin/env python3
"""
task: 14. Top students
condition: #advanced
required:
Write a Python function that returns all students sorted by average score:

    Prototype: def top_students(mongo_collection):
    mongo_collection will be the pymongo collection object
    The top must be ordered
    The average score must be part of each item returns with key = averageScore
"""


def top_students(mongo_collection):
    """
    inserts a new document in a collection based on kwargs

    Args:
        mongo_collection (db colllection): the pymongo collection object

    Returns:
        list of school having a specific topic
    """

    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])


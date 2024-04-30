#!/usr/bin/env python3
"""
task: 11. Where can I learn Python?
condition: mandatory
required:
Write a Python script that provides some stats about Nginx logs stored
in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
in this order (see example below - warning: it's a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
"""
from pymongo import MongoClient


def helper(mongo_collection):
    """
    helper function to do the required
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{mongo_collection.estimated_document_count()} logs \nMethods:")

    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    n_logs = MongoClient.count_documents({
        "method": "GET", "path": "/status"
    })
    print(f"{n_logs} status check")


if __name__ == "__main__":
    client = MongoClient()

    db = client.logs
    collection = db.nginx

    helper(collection)

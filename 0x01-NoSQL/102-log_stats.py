#!/usr/bin/env python3
"""
task: 5. Log stats - new version
condition: advanced
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


def log_nginx_stats(mongo_collection):
    """
    helper function
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{mongo_collection.estimated_document_count()} logs")

    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    number_of_gets = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{number_of_gets} status check")

    top_ips = mongo_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print(f'\t{ip}: {count}')


if __name__ == "__main__":
    mongo_collection = MongoClient().logs.nginx
    log_nginx_stats(mongo_collection)

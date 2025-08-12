#!/usr/bin/env python3
"""
Module for providing stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides stats about Nginx logs stored in MongoDB, including total logs,
    method counts, status checks, and top 10 IPs by frequency.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Total number of logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count of each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count of GET requests to /status
    status_checks = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_checks} status check")

    # Top 10 IP by frequency
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = logs_collection.aggregate(pipeline)
    print("IPs:")
    for ip_doc in top_ips:
        print(f"\t{ip_doc['_id']}: {ip_doc['count']}")


if __name__ == "__main__":
    log_stats()

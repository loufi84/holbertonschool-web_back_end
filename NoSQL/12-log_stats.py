#!/usr/bin/env python3
"""
This module provides stats about Nginx logs in MongoDB
"""


from pymongo import MongoClient

def main():
    """
    The method to provide the stats of logs stored in MongoDB
    """
    client = MongoClient('mongodb://localhost:27017')
    logs = client.logs.nginx

    total_logs = logs.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_checks = logs.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

if __name__ == "__main__":
    main()

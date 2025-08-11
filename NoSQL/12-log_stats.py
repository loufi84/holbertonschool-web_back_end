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
    db = client.logs
    nginx = db.nginx

    total_logs = nginx.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{total_logs} logs")
    print("Methods:")

    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_checks = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")

    client.close()

if __name__ == "__main__":
    main()

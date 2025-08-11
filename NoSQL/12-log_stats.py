#!/usr/bin/env python3
"""
Module for providing stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    nginx_collection = client.logs.nginx

    # Get counts
    number = nginx_collection.count_documents({})
    number_get = nginx_collection.count_documents({"method": "GET"})
    number_post = nginx_collection.count_documents({"method": "POST"})
    number_put = nginx_collection.count_documents({"method": "PUT"})
    number_patch = nginx_collection.count_documents({"method": "PATCH"})
    number_delete = nginx_collection.count_documents({"method": "DELETE"})
    number_status = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Print results in the exact format
    print("{} logs".format(number))
    print("Methods:")
    print("\tmethod GET: {}".format(number_get))
    print("\tmethod POST: {}".format(number_post))
    print("\tmethod PUT: {}".format(number_put))
    print("\tmethod PATCH: {}".format(number_patch))
    print("\tmethod DELETE: {}".format(number_delete))
    print("{} status check".format(number_status))

#!/usr/bin/env python3
""" Provides stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

if __name__ == "__main__":
    """ Connect to MongoDB and retrieve Nginx log stats """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    """ Print total number of logs """
    print(f"{collection.count_documents({})} logs")

    """ Print method stats """
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    """ Print status check stats """
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
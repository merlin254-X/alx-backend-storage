#!/usr/bin/env python3

"""A Python module that provides stats about nginx"""

from pymongo import MongoClient


if __name__ == '__main__':
    """Prints the log stats in nginx collection"""
    con = MongoClient('mongodb://localhost:27017')
    collection = con.logs.nginx

    """Print the total number of logs"""
    print(f'{collection.estimated_document_count()} logs')

    """Print method stats"""
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')
    for req in methods:
        print(f'\tmethod {req}: {collection.count_documents({"method": req})}')

    """Print the number of status check logs"""
    print(f'{collection.count_documents({"method": "GET", "path": "/status"})} status check')

    """Top 10 most frequent IPs"""
    print('IPs:')
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)

    """Print top 10 IPs"""
    for ip in top_ips:
        print(f'\t{ip["_id"]}: {ip["count"]}')

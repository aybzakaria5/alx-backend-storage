#!/usr/bin/env python3
"""task 12"""
import pymongo

# Connect to local MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

# Get total number of logs
total_logs = collection.count_documents({})

print(f"{total_logs} logs")

# Count methods
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"method {method}: {count}")

# Count status check
status_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_count} status check")


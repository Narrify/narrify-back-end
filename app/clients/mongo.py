"""
TODO
"""
from gc import collect

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["db"]
collection = db["collection"]

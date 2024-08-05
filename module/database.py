import os
from random import randint
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
usr = os.getenv('MONGODB_USR')
pwd = os.getenv('MONGODB_PWD')
host = os.getenv('MONGODB_HOST')
uri = f"mongodb+srv://{usr}:{pwd}@{host}"

client = MongoClient(uri)
user_db = client.test

def insert_new_user():
    test_collection = user_db.test
    user = {
        "_id": randint(1, 100000),
        "name": "Son Nguyen",
        "age": 19
    }
    test_collection.insert_one(user)

for i in range(1, 10):
    insert_new_user()
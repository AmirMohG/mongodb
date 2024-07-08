from pymongo import MongoClient
import os

mongo_url = os.getenv('MONGO_URI', 'mongodb://root:adminamin@corleone110-a1d1.corleone110.svc:27017')

client = MongoClient(mongo_url)
db = client.get_default_database()


collection = db.persons
result =  collection.insert_one({"name": "amin", "age": 20})

print(result.inserted_id)

client.close()

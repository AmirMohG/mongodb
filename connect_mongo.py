from pymongo import MongoClient


client = MongoClient('mongodb://root:adminamin@212.80.20.179:30888/')
# create database
db = client.mydatabase
# create collection
collection = db.persons
result = collection.insert_one({"name": "amin", "age": 20})

print(result.inserted_id)

find = collection.find_one({"name": "amin"})
print(find)

client.close()

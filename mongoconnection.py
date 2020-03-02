from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["kiran"]
mycollection=db["employee"]
emp = {
    "id": 1,
    "Name": "asd"
}
empl=mycollection.insert_one(emp)

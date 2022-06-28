
from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()  # take environment variables from .env.
MONGODB_PASSWORD = getenv("MONGODB_PASSWORD")

client = MongoClient(f"mongodb+srv://corylr:{MONGODB_PASSWORD}@cluster0.uxodstt.mongodb.net/?retryWrites=true&w=majority")

blew_a_fuse_db = client.get_database("blewafuse")
test_collection = blew_a_fuse_db.get_collection("test")

# print(test_collection.insert_one({"foo": "bar"}))
print(test_collection.find_one({"hello": "world"}))



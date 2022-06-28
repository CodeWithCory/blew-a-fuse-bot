
from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import FastAPI

# Environment Variables
load_dotenv()
MONGODB_PASSWORD = getenv("MONGODB_PASSWORD")

# Database
client = MongoClient(f"mongodb+srv://corylr:{MONGODB_PASSWORD}@cluster0.uxodstt.mongodb.net/?retryWrites=true&w=majority")
blew_a_fuse_db = client.get_database("blewafuse")
test_collection = blew_a_fuse_db.get_collection("test")
first_document = test_collection.find_one({"hello": "world"})

# Server
app = FastAPI()
@app.get("/")
async def root():
    return {"hello": first_document["hello"]} # Expect value "world" from database
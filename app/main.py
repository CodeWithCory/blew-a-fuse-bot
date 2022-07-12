
from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient
from fastapi import FastAPI
import tweepy

# Environment Variables
load_dotenv()
MONGODB_PASSWORD = getenv("MONGODB_PASSWORD")
TWITTER_CONSUMER_API_KEY = getenv("TWITTER_CONSUMER_API_KEY")
TWITTER_CONSUMER_API_KEY_SECRET = getenv("TWITTER_CONSUMER_API_KEY_SECRET")
TWITTER_ACCESS_TOKEN = getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Database
# IP Address must be allowed at https://cloud.mongodb.com/ -> Network Access
# client = MongoClient(f"mongodb+srv://corylr:{MONGODB_PASSWORD}@cluster0.uxodstt.mongodb.net/?retryWrites=true&w=majority")
# blew_a_fuse_db = client.get_database("blewafuse")
# test_collection = blew_a_fuse_db.get_collection("test")
# first_document = test_collection.find_one({"hello": "world"})

# Twitter
auth=tweepy.OAuthHandler(TWITTER_CONSUMER_API_KEY, TWITTER_CONSUMER_API_KEY_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
bot_api=tweepy.API(auth)
# bot_api.update_status('Hello, world!')

# Server
app = FastAPI()
# @app.get("/")
# async def root():
#   return {"hello": first_document["hello"]} # Expect value "world" from database

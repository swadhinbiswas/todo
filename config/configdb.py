import motor.motor_asyncio as m
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv,find_dotenv
import os
load_dotenv(find_dotenv())

username=os.environ.get('MONGO_USER')

password=os.environ.get('MONGO_PASSWORD')

host=os.environ.get('MONGO_HOST')

url=f"mongodb+srv://{username}:{password}@{host}/test?retryWrites=true&w=majority"

client=m.AsyncIOMotorClient(url,serverApi=ServerApi('1'))
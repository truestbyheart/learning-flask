from pymongo import MongoClient

from config import MONGODB_URI

def getDbInstance():
    client = MongoClient(MONGODB_URI)
    return client['sentences']
    

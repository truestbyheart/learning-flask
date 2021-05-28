from pymongo import MongoClient

def getDbInstance():
    client = MongoClient('mongodb://sentence:LIVE101wm@localhost:27017')
    return client['sentences']
    

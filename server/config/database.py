import pymongo

def connectDB():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient["mydatabase"]
    return db
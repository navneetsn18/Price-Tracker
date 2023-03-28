import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client.get_database('price-tracker')
collection = db.userdata


def addUser(args):
    if collection.find_one({"username": args["username"]}):
        return {"message": "User Already Exists!!"}
    else:
        data = {
            "username": args["username"],
            "track": []
        }
        collection.insert_one(data)
        return {"message": "User Added --> "+args["username"]}


def deleteUser(args):
    if collection.find_one({"username": args["username"]}):
        collection.delete_one({"username": args["username"]})
        return {"message": "User Deleted Successfully --> "+args["username"]}
    else:
        return {"message": "User Does Not Exists"}

def updateUser(args):
    if collection.find_one({"username": args["oldusername"]}):
        collection.update_one({"username": args["oldusername"]},{"$set":{"username": args["newusername"]}})
        return {"message": "Username Updated from --> "+args["oldusername"]+" to "+args["newusername"]}
    else:
        return {"message": "User Does Not Exists"}


def getUser(args):
    if collection.find_one({"username": args["username"]}):
        return collection.find_one({"username": args["username"]})
    else:
        return {"message": "User Does Not Exists"}


def getAllUsers(args):
    # users = {}
    # for i, data in enumerate(list(collection.find())):
    #     users[i+1] = data["username"]
    # return users
    return collection.find()

import os
import uuid
from pymongo import MongoClient
from dotenv import load_dotenv
import modules.extractor.Amazon as Amazon
import modules.extractor.Flipkart as Flipkart
import modules.extractor.Myntra as Myntra

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client.get_database('price-tracker')
collection = db.userdata


def addProduct(args):
    if collection.find_one({"username": args["username"]}):
        products = collection.find_one({"username": args["username"]})["track"]
        data = {}
        if "amazon" in str(args.get('url')):
            try:
                data = Amazon.getAmazonData(args.get('url'))
            except:
                return {"message": "No Data Found For The Given Url"}
        elif "flipkart" in str(args.get('url')):
            try:
                data = Flipkart.getFlipkartData(args.get('url'))
            except:
                return {"message": "No Data Found For The Given Url"}
        elif "myntra" in str(args.get('url')):
            try:
                data = Myntra.getMyntraData(args.get('url'))
            except:
                return {"message": "No Data Found For The Given Url"}
        else:
            return {"message": "Currently We Do Not Support This Site"}
        if data != {}:
            for product in products:
                if product["name"] == data["name"]:
                    return {"message": "Product Already Added"}
            trackingData = {
                "id": uuid.uuid4().hex,
                "name": data["name"],
                "target": args.get('target'),
                "url": args.get('url')
            }
            collection.update_one({"username": args["username"]}, {
                                  "$push": {"track": trackingData}})
        else:
            return {"message": "No Data Found For The Given Url"}
        return {"message": "Tracking Started For --> "+data["name"]}
    else:
        return {"message": "User Does Not Exists"}


def updateProduct(args):
    if collection.find_one({"username": args["username"]}):
        products = collection.find_one({"username": args["username"]})["track"]
        for product in products:
            if product['id'] == args.get("id"):
                collection.update_one({"username": args["username"], "track.id": args["id"]},
                                      {"$set": {"track.$.target": args.get("target")}})
                return {"message": "Updated "+product['name']+" for --> "+args["username"]}
        return {"message": "Incorrect ID!!"}
    else:
        return {"message": "User Does Not Exists"}

    # {"username": args["username"]},{"track": {"id": args.get('id')}} {"$set": {}}


def deleteProduct(args):
    if collection.find_one({"username": args["username"]}):
        products = collection.find_one({"username": args["username"]})["track"]
        for product in products:
            if product['id'] == args.get("id"):
                collection.update_one({"username": args["username"]}, {
                    "$pull": {"track": {"id": args.get('id')}}})
                return {"message": "Deleted "+product['name']+" for --> "+args["username"]}
        return {"message": "Incorrect ID!!"}
    else:
        return {"message": "User Does Not Exists"}


def deleteAllProducts(args):
    if collection.find_one({"username": args["username"]}):
        collection.update_one({"username": args["username"]}, {
            "$pull": {"track": {}}})
        return {"message": "Deleted All Products For --> "+args["username"]}
    else:
        return {"message": "User Does Not Exists"}

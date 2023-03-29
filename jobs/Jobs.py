import os
from pymongo import MongoClient
from dotenv import load_dotenv
import modules.extractor.Amazon as Amazon
import modules.extractor.Flipkart as Flipkart
import modules.extractor.Myntra as Myntra
import modules.mail.Mail as Mail

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db = client.get_database('price-tracker')
count_collection = db.count

def check(args):
    count = int(count_collection.find_one()["count"])
    if count>=int(db.timer.find_one()["timer"]):
        count = 1
        db.tracked_today.update_one({},{"$set": {"today": []}})
    else:
        count+=1
    count_collection.update_one({},{"$set": {"count": count}})
    
    collection = db.userdata.find()

    for userdata in collection:
        items = userdata["track"]
        currect_data = {}
        for item in items:
            if "amazon" in item["url"]:
                try:
                    currect_data = Amazon.getAmazonData(item["url"])
                except:
                    print({"message": "No Data Found For The Given Url"})
            elif "flipkart" in item["url"]:
                try:
                    currect_data = Flipkart.getFlipkartData(item["url"])
                except:
                    print({"message": "No Data Found For The Given Url"})
            elif "myntra" in item["url"]:
                try:
                    currect_data = Myntra.getMyntraData(item["url"])
                except:
                    print({"message": "No Data Found For The Given Url"})
            if currect_data["price"]<=float(item["target"]):
                if item["id"] not in list(db.tracked_today.find_one()["today"]):
                    db.tracked_today.update_one({},{"$push": {"today": item["id"]}})
                    Mail.sendEmail(userdata["username"],userdata["email"],item["name"],item["url"],currect_data["price"])
    return {"message" : "success"}
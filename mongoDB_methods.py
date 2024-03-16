import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

mongoPassword = os.getenv('MONGO_PASSWORD')  #Load key from secret

client = pymongo.MongoClient(f"mongodb+srv://warwolf:{mongoPassword}@cluster0.gis05ag.mongodb.net/")
db = client.Business_Cards_Lake


cards_table = db.cards



def insert_into_mdb(card_data):
    try:
        cards_table.insert_one(card_data)
    except:
        print("Failed mongodb")

def channel_names():
    ch_name = []
    for i in db.channels.find():
        ch_name.append(i['Channel_name'])
    return ch_name

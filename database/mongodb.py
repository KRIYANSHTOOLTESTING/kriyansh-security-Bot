# 📁 database/mongodb.py
from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client['roseplusplus']

# ✅ Collections
groups = db.groups
users = db.users
feds = db.federations
confessions = db.confessions

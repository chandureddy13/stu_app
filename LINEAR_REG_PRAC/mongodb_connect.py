import urllib.parse
from pymongo import MongoClient

# Encode username and password
username = urllib.parse.quote_plus("chandureddy2579")
password = urllib.parse.quote_plus("K.madan@10121963")  # Escape special characters

# Corrected MongoDB URI
MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.9zkya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Check connection
try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection failed:", e)

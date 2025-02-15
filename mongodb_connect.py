from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse

# Encode username and password
username = urllib.parse.quote_plus("chandureddy2579")
password = urllib.parse.quote_plus("K.madan@10121963")

# Construct the encoded URI
uri = f"mongodb+srv://{username}:{password}@cluster0.9zkya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

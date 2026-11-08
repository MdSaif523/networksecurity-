from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://mds744007_db_user:Admin123@cluster0.kng6qf7.mongodb.net/"

# Create a new MongoClient
client = MongoClient(uri)

# send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
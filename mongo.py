

from pymongo import MongoClient


class MongoDBConnector:

    """
    For connect MongoDB Database
    """

    URL = "mongodb+srv://db:qpMyBjC0qbNCl4M2@cluster0.gx0on.mongodb.net/jam?authSource=admin&replicaSet=atlas-leaocf-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"

    client = MongoClient(URL)
    db = client.get_database("jam")

    @classmethod
    def connect(cls) -> MongoClient:
        print("Mongodb:=> connected!")
        return cls.db

    @classmethod
    def disconnect(cls):
        print("Mongodb:=> disconnected!")
        return cls.client.close()

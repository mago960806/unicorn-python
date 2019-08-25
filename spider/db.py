from pymongo import MongoClient


class MongoDB(object):

    def __init__(self, host, port: int, db_name, collection_name):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name

    def __enter__(self):
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]
        return self.collection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

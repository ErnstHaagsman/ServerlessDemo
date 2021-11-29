from pymongo import MongoClient

CXN = "mongodb://demo:hunter2@mongo.guestbook.teamcity.com/myDB?retryWrites=true&w=majority"


class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(CXN)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

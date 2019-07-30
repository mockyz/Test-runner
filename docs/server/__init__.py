# -*- coding: utf-8 -*-
from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
db = mongo_client.napos_apis


class BaseCollection():
    collection_name = ''

    def __init__(self):
        self.collection_doc = {}

    def insert_one(self):
        return db[self.collection_name].insert_one(self.collection_doc)

    def find(self, params={}):
        return db[self.collection_name].find(params)

    def update_or_insert(self):
        raise NotImplemented("not implemented in base class")

    def update_one(self, search_criteria):
        return db[self.collection_name].update_one({
            search_criteria,
            {"$set": self.collection_doc}
        })

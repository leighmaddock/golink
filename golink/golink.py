#!/usr/bin/env python
from pymongo import mongo_client

class golink:
    def __init__(self, dbname="golinkdb", host="localhost", port=27017):
        self.dbname = dbname
        self.conn = mongo_client.MongoClient(host, port)
        self.db = self.conn[dbname]
        self.items = self.db.golinks

    def add(self, link, linkto, meta={}):
        updates = {}
        updates["linkto"] = linkto
        updates.update(meta)
        self.items.find_and_modify({"link": link}, {"$set": updates}, upsert=True)

    def remove(self, link):
        self.items.find_and_modify({"link": link}, remove=True)

    def fetch(self, link):
        linkto = ""
        results = self.items.find_one({"link": link})
        if results:
            linkto = results["linkto"]
        return linkto

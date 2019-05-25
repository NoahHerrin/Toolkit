import pymongo


class Database(object):
    def __init__(self,collection,attributes):
        client = pymongo.MongoClient("mongodb+srv://herrinn:root123@practice-yqlip.mongodb.net/test?retryWrites=true")
        self.db = client["smartypants"]
        self.collection = self.db[collection]
        self.attributes = attributes

    # using the provided attributes will check if collection contains document
    def contains(self, data):
        # check for name, color, type
        for trait in self.attributes['titles']:
            if trait in data and self.fetch(trait, data[trait]).count() is 1:
                return True
        return False

    # provide a key and a value, will fetch associated document
    def fetch(self, key, value):
        query = {key : value}
        response = self.collection.find_one(query)
        return response

    # insert a dictionary of data into collection
    def insert(self,data):
        data['id'] = self.fetch_num_entries() + 1
        return self.collection.insert_one(data)

    # returns all entries in collection
    def fetch_all_entries(self):
        return self.collection.find()

    # return the number of entries in collection
    def fetch_num_entries(self):
        return self.collection.count()
    def fetch_settings(self):
        return self.attributes
    

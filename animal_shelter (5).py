from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser1'
        PASS = 'Station140'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = '30032'
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,int(PORT)))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)  # data should be a dictionary
                return True
            except Exception as e:
                print(f"An error occurred during insertion: {e}")
                return False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, query):
        try:
            result = self.collection.find(query)
            if result is not None:
                return list(result)
            else:
                print("Nodata found.")
                return []# query should be a dictionary
        except Exception as e:
            print(f"An error occurred during querying: {e}")
            return []
    
    def update(self, query, update_data, multi=False):
        try:
            if multi:
                result = self.collection.update_many(query, {'$set': update_data})
                return result.modified_count
            else:
                result = self.collection.update_one(query, {'$set': update_data})
                return result.modified_count
        except Exception as e:
            print(f"An error occurred during update: {e}")
            return 0

    def delete(self, query, multi=False):
        try:
            if multi:
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                result = self.collection.delete_one(query)
                return result.deleted_count
        except Exception as e:
            print(f"An error occurred during deletion: {e}")
            return 0


import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self,username=None,password=None):
        
        #self.client = MongoClient("mongodb://127.0.0.1:48093/AAC" % (username,password))
        self.client = MongoClient("mongodb://aacuser:tennis21@127.0.0.1:48093/?authSource=AAC")
        self.database=self.client['AAC']
   
      
    
        #if username and password:
            #self.client=MongoClient('mongodb://%s:%s@localhost:48093'%(username,password))
            #print(self.client.list_database_names())
            
            
        #else:
            #self.client=MongoClient('mongodb://%s:%s@localhost:48093')
            
        #self.database=self.client['AAC']
        
        #where xxx is your unique port number
        
        
 # Complete this create method to implement the C in CRUD.
    def create(self,data):
        if data is not None:
            print(data)
            self.database.animals.insert(data)
            print("Success")
            return True
            
        else: raise Exception("Nothing to save because data parameter is empty")
        
            

            
    def read(self,data):
        if data is not None:
            print("being read")
            print(data)
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("Nothing to read because data parameter is empty")
            
    def update(self,currentData,changesToBeMade):
        if currentData is not None and changesToBeMade is not None: #If criteria is not null, update all entries that fit currentData parameter with changesToBeMade parameter. Then return the results. If criteria is empty, raise an exception.
            self.database.animals.update_many(currentData,changesToBeMade)
            print("update complete")
            return self.database.animals.find(currentData)    
        else:
            raise Exception ("Noting to read because data parameter is empty")
            

    def delete(self,data): #If data isn't null delete all entries that match the criteria otherwise don't delete anything. If criteria is empty, raise an exception
        if data is not None:
            self.database.animals.delete_many(data)
            print("delete successful")
            return self.database.animals.find(data) 
        else:
            raise Exception("Nothing to delete because data parameter is empty")
            
          
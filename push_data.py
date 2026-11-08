import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL") # Means gettting the environment variable from .env file.
print(MONGO_DB_URL)

import certifi
import pymongo

ca=certifi.where()

import pandas as pd
import numpy as np

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def cv_to_json_convertor(self,file_path:str)->json:
        """
        This function will convert the csv file to json format.
        """
        try:

            data=pd.read_csv(file_path)# Reading the csv file using pandas.
            data.reset_index(drop=True,inplace=True) #Resetting the index of the dataframe and dropping the old index. 
            records=list(json.loads(data.T.to_json()).values()) # Converting dataframe into list of json records.
            logging.info(f"Data converted to JSON successfully from {file_path}.")
            return records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongodb(self,records,database,collection):
        """
        This function will insert the data into mongodb collection.
        """
        try:
           self.database=database
           self.collection=collection
           self.records=records

           self.mongo_client=pymongo.MongoClient(MONGO_DB_URL) # Creating a connection to mongodb using pymongo.
           self.database=self.mongo_client[self.database] # Creating a database in mongodb.

           self.collection=self.database[self.collection] # Creating a collection in mongodb.
           self.collection.insert_many(self.records) # Inserting the records into the collection.
           return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__=='__main__':
    FILE_PATH=r"D:\Network Security\Network_Data\phisingData.csv"
    DATABASE="SAIFUAI"
    collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print("Records to be inserted:",records)
    no_of_records=networkobj.insert_data_to_mongodb(records=records,database=DATABASE,collection=collection)
    print(f"Number of records inserted: {no_of_records}")
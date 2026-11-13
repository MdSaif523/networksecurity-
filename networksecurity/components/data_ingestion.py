from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

## configuration of the data ingestion Config.

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os
import pandas as pd 
import sys
import numpy as np
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv() # Load the environment variables from dotenv file.

MONGO_DB_URL=os.getenv("mongodb+srv://mds744007_db_user:Admin123@cluster0.kng6qf7.mongodb.net/") # Get the MongoDB URL from environment variable.


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys) 


    def export_collection_as_dataframe(self):
        # here, we'll go ahead and fetch and read the data from mongodb and convert it into pandas dataframe.
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]

            df=pd.DataFrame(list(collection.find())) # It means, collection ke andar jo bhi data hai, usko list me convert kar ke dataframe me convert kar do.
        
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"],axis=1)

            df.replace({"na":np.nan},inplace=True) # It means, dataframe me jo bhi "na" hai, usko np.nan me convert kar do.
            logging.info(f"Dataframe is created from the collection: {collection_name} in database")
            return df
    
        except Exception as e:
            raise NetworkSecurityException(e,sys) 


    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            
            # Creating folder 'feature_store_file_path'.
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)

            # Saving dataframe to the feature_store_file_path as 'csv' file.
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            logging.info(f"Data is saved to the feature store: {feature_store_file_path}")
            return dataframe

        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(
                dataframe,test_size=self.data_ingestion_config.train_test_split_ratio,random_state=42
            )

            logging.info(f"Data is splitted into train and test set")

            logging.info("Exited split_data_as_train_test method of Data_Ingestion class .")

            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path,exist_ok=True)

            logging.info("Exporting train and test file path.")

            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)

            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info("Exported train and test file path.")
            
            return train_set,test_set
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            data_ingestion_artifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                          test_file_path=self.data_ingestion_config.testing_file_path)

            return data_ingestion_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys) 
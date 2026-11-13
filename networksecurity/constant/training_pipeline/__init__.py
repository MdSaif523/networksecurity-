import os
import sys
import numpy as np

"""
Defining the constant variables for training pipeline.
"""

TARGET_COLUMN="Result"
PIPELINE_NAME:str="networksecurity" # Pipeline name for training pipeline.
ARTIFACTS_DIR:str="artifacts" # Artifacts directory name for training pipeline.

FILE_NAME:str="phisingData.csv" # File name for training pipeline.
TRAIN_FILE_NAME:str="train.csv" # Train file name for training pipeline.
TEST_FILE_NAME:str="test.csv" # Test file name for training pipeline.


SCHEMA_FILE_PATH=os.path.join("join_schema","schema.yaml")
# It means entire schema.yaml file present inside join_schema folder.

SAVED_MODEL_DIR=os.path.join("saved_models")

MODEL_FILE_NAME="model.pkl"



''' 
Data Ingestion Related constant starts with DATA_INGESTION VARAIBLE NAME.
'''

DATA_INGESTION_COLLECTION_NAME:str="NetworkData" # Collection name in mongodb.
DATA_INGESTION_DATABASE_NAME:str="SAIFUAI" # Database name in mongodb.
DATA_INGESTION_DIR_NAME:str="data_ingestion" # Directory name for data ingestion.
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store" # Directory name for feature store.
DATA_INGESTION_INGESTED_DIR:str="ingested" # Directory name for ingested data.
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIOS:float=0.2 # Train test split ratio.


'''
Data Validation Related constant starts with DATA_VALIDATION VARIABLE NAME.
'''

DATA_VALIDATION_DIR_NAME: str="data_validation"
DATA_VALIDATION_VALID_DIR: str="validated"
DATA_VALIDATION_INVALID_DIR: str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str="report.yaml"
PREPROCESSING_OBJECT_FILE_NAME:str="preprocessing.pkl"

'''
Data Transformation related constant starts with DATA_TRANSFORMATION VARIABLE NAME.
'''
DATA_TRANSFORMATION_DIR_NAME: str= "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str="transformed_object"

# knn imputer class basically used to replace 'nan' values.
DATA_TRANSFORMATION_IMPUTER_PARAMS:dict={
    "missing values":np.nan,
    "n_neighbours":3,
    "weights":"uniform",
}



'''
Model Trainer related constant starts with MODEL_TRAINER VARIABLE NAME.
'''

MODEL_TRAINER_DIR_NAME: str= "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR :str= "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME :str= "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float=0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD: float = 0.05


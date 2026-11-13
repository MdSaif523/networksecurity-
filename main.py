from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig,ModelTrainerConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from networksecurity.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
import sys

if __name__=='__main__':
    try:

        ## Applying Data-Ingestion.
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion.")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation Completed.")


        ## Applying and joining Data-Validation with Data_ingestion.
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation.")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed.")


        ## Applying and joining Data-Transformation with Data_Validation.
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation,data_transformation_config)
        logging.info("Initiate the data Transformation.")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed.")
        print(data_transformation_artifact)


        ## Applying and joining Model Training with Data_transformation.
        logging.info("Model Training Started.")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model Training Artifact created.")

        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
import os
import sys
from logger import logging
from exception import CustomException
import pandas as pd

from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer
from components.model_evaluation import ModelEvaluation

logging.info('Training pipeline started')

try : 
    logging.info('Data ingestion initiated')
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

    logging.info('Data transformation initiated')
    data_transformation = DataTransformation()
    train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    logging.info('Model trainer initiated')
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_training(train_arr, test_arr)

    logging.info('Model evaluator initiated')
    model_evaluation = ModelEvaluation()
    model_evaluation.initiate_model_evaluation(train_arr, test_arr)
except Exception as e:
    logging.info('!!! Error inside training pipeline')
    CustomException(e, sys)

logging.info('Training pipeline completed')
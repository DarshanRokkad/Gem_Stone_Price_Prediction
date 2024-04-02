import os
import sys
from logger import logging
from exception import customexception
import pandas as pd

from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer
from components.model_evaluation import ModelEvaluation

logging.info('Training pipeline started')

data_ingestion = DataIngestion()
train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

data_transformation = DataTransformation()
train_arr, test_arr = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

model_trainer = ModelTrainer()
model_trainer.initiate_model_training(train_arr, test_arr)

model_evaluation = ModelEvaluation()
model_evaluation.initiate_model_evaluation(train_arr, test_arr)

logging.info('Training pipeline completed')
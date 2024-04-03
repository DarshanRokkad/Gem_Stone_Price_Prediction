import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

import mlflow
import mlflow.sklearn
from sklearn.metrics import r2_score, mean_squared_error,mean_absolute_error
from src.utils import load_obj
from urllib.parse import urlparse


@dataclass
class ModelEvaluationConfig:
    trained_model_file_path:str = os.path.join('artifacts','model.pkl')

class ModelEvaluation:   
    def __init__(self):
        self.model_evaluation_config = ModelEvaluationConfig()
     
    def evaluation_metrics(self, actual, predicted):
        r2 = r2_score(actual, predicted)
        mse = mean_squared_error(actual, predicted)
        mae = mean_absolute_error(actual, predicted)
        return (r2, mse, mae)
    
    def initiate_model_evaluation(self, train_arr, test_arr):
        try:
            logging.info('Model evaluation started')
            
            x_test, y_test = test_arr[:, :-1], test_arr[:, -1]
            model = load_obj(self.model_evaluation_config.trained_model_file_path)
            logging.info('Model loaded successfully')
            
            # mlflow.set_registry_uri("")
            logging.info('Model has registered')
            
            tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            logging.info(f"{tracking_uri_type_store}")
            
            with mlflow.start_run():
                prediction = model.predict(x_test)
                r2, mse, mae = self.evaluation_metrics(y_test, prediction)
                mlflow.log_metric('r2 score', r2)
                mlflow.log_metric('Mean squared error', mse)
                mlflow.log_metric('Mean absolute error', mae)                
                if tracking_uri_type_store != 'file':
                    mlflow.sklearn.log_model(model, 'model', registered_model_name = "ml_model")       # Register the model
                else:
                    mlflow.sklearn.log_model(model, 'model')
            
            logging.info('Model evaluation completed')
        except Exception as e:
            logging.info('!!! Error in model evaluation')
            CustomException(e, sys)
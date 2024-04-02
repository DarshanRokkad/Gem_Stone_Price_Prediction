import os
import sys
from logger import logging
from exception import CustomException
from dataclasses import dataclass
from utils import save_obj, evaluate_models

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import r2_score


@dataclass
class ModelTrainerConfig:
    trained_model_file_path:str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_array, test_array) -> None:
        try:
            logging.info('Model training started')

            logging.info('train test array split initiated')
            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            logging.info('All model creation initiated')
            models = {
                'Linear Regressor' : LinearRegression(), 
                'Ridge Regressor' : Ridge(), 
                'Lasso Regressor' : Lasso(), 
                'ElasticNet Regressor' : ElasticNet()
            }

            models_report, best_model_name, best_model_score = evaluate_models(x_train, x_test, y_train, y_test, models)            
            logging.info(f'{models_report}')
            logging.info(f'Best model is {best_model_name} with r2 score {best_model_score}')

            logging.info('Checking whether best model score is more than threshold')
            if best_model_score < 0.6:
                logging.info('Best model score does not cross threshold so no best model exhist')
                raise CustomException('No best model found', sys)

            logging.info('Best model training, prediction and accuracy')
            best_model = models[best_model_name]
            best_model.fit(x_train, y_train)
            y_pred = best_model.predict(x_test)
            r2_sco = r2_score(y_test, y_pred)
            logging.info(f'{best_model_name} accracy = {r2_sco}')

            logging.info(f'Saving {best_model_name} model')
            save_obj(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
            
            logging.info('Model training completed')
        except Exception as e:
            logging.info('!!! Error occured in model training')
            raise CustomException(e, sys)
import os
import sys
from logger import logging
from exception import CustomException
import dill

from sklearn.metrics import r2_score

def save_obj(file_path:str, obj) -> None:
    ''' save the given object in the given file path '''
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
        logging.info('Object saved successfully')
    except Exception as e:
        logging.info('!!! Error occured in save object')
        raise CustomException(e, sys)
    
def load_obj(file_path:str):
    ''' loads the object from the given file path '''
    try:
        with open(file_path, 'rb') as file:
            obj = dill.load(file)
        logging.info('Object loaded successfullys')
        return obj
    except Exception as e:
        logging.info('!!! Error occured in loading object')
        raise CustomException(e, sys)
    
def evaluate_models(x_train, x_test, y_train, y_test, models):
    ''' Evaluates the given models and return r2 score of the models '''
    try:
        logging.info('Model evaluation starts')
        
        report = {}
        best_model_name, best_model_score = None, 0
        for model_name in models:
            logging.info(f'Training {model_name} model started')
            regressor = models[model_name]
            regressor.fit(x_train, y_train)
            y_pred = regressor.predict(x_test)
            r2 = r2_score(y_test, y_pred)
            report[model_name] = r2
            if r2 > best_model_score:                
                best_model_name = model_name
                best_model_score = r2
            logging.info(f'Training {model_name} model completed')
            
        logging.info('Model evaluation completed')        
        return report, best_model_name, best_model_score
    except Exception as e:
        logging.info('!!! Error occured in evaluating model')
        CustomException(e, sys)
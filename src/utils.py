import os
import sys
from logger import logging
from exception import CustomException
import dill


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
        with open(file_path, 'wb') as file:
            obj = dill.load(file)
        logging.info('Object loaded successfullys')
        return obj
    except Exception as e:
        logging.info('!!! Error occured in loading object')
        raise CustomException(e, sys)
    

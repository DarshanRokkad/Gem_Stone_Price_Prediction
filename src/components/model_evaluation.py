import os
import sys
from logger import logging
from exception import CustomException

class ModelEvaluation:
    def initiate_model_evaluation(self, train_arr, test_arr):
        try:
            logging.info('Model evaluation started')
            
            logging.info('Model evaluation completed')
        except Exception as e:
            logging.info('!!! Error in model evaluation')
            CustomException(e, sys)
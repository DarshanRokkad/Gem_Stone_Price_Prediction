import os
import sys
from exception import CustomException
from logger import logging
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.dataingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info('Data ingestion started')
        try:
            raw_df = pd.read_csv('https://raw.githubusercontent.com/DarshanRokkad/Gem_Stone_Price_Prediction/master/notebooks/dataset/gemstone.csv')
            logging.info('Data read successfully')
            
            file_dir = os.path.dirname(self.dataingestion_config.raw_data_path)
            os.makedirs(file_dir, exist_ok = True)
            
            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(raw_df, test_size = 0.25, random_state = 42)
            
            raw_df.to_csv(self.dataingestion_config.raw_data_path, index = False, header = True)
            train_set.to_csv(self.dataingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.dataingestion_config.test_data_path, index = False, header = True)
            
            logging.info('Data ingestion completed')
            return (
                self.dataingestion_config.train_data_path,
                self.dataingestion_config.test_data_path
            )
        except Exception as e:
            logging('!!! Error occured in data ingestion')
            raise CustomException(e, sys)
        
        
# for testing purpuse only 
if __name__ ==  '__main__':
    # checking data ingestion
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()
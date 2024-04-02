import os
import sys
from exception import CustomException
from logger import logging
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from utils import save_obj

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.datatransformation_config = DataTransformationConfig()
        
    def get_preprocessor_obj(self):
        ''' Returns the preprocessor object '''
        try:
            logging.info('Creation of preprocessor object started')
            
            numerical_features = ['carat', 'depth', 'table', 'x', 'y', 'z']
            categorical_features = ['cut', 'color', 'clarity']
            
            logging.info('Numerical and categorical pipeline creation initiated')
            numerical_pipeline = Pipeline(
                steps = [
                    ('step 1 : Handling missing values', SimpleImputer(strategy = 'median')),
                    ('step 2 : Standard Scaling', StandardScaler())
                ]
            )
            cut_category = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_category = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_category = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
            categorical_pipeline = Pipeline(
                steps = [
                    ('step 3 : Handling missing values', SimpleImputer(strategy = 'most_frequent')),
                    ('step 4 : Ordinal Encoding', OrdinalEncoder(categories = [cut_category, color_category, clarity_category]))
                ]
            )
            
            logging.info('Column Transoformer creation initiated')
            preprocessor_obj = ColumnTransformer(
                [
                    ('Numerical Pipeline', numerical_pipeline, numerical_features),
                    ('Categorical Pipeline', categorical_pipeline, categorical_features)
                ]
            )
            
            logging.info('Creation of preprocessor object completed')
            return preprocessor_obj
        except Exception as e:
            logging.info('!!! Error occured in creating preprocessor object')
            CustomException(e, sys)
    
    def initiate_data_transformation(self, train_data_path:str, test_data_path:str):
        try:            
            logging.info('Data transformation started')
            
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            logging.info('Training data and test data read successfully')
            
            logging.info('Separating independent and dependent feature')
            dependent_feature = 'price'
            independent_feature_train_df = train_df.drop(columns = [dependent_feature], axis = 1)
            dependent_feature_train_df = train_df[dependent_feature]
            independent_feature_test_df = test_df.drop(columns = [dependent_feature], axis = 1)
            dependent_feature_test_df = test_df[dependent_feature]
            
            logging.info('Data preprocessing initiated')
            preprocessor_obj = self.get_preprocessor_obj()
            input_feature_train_arr = preprocessor_obj.fit_transform(independent_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(independent_feature_test_df)
            train_arr = np.c_[input_feature_train_arr, np.array(dependent_feature_train_df)]           # concatinate data transformed training feature with output feature 
            test_arr = np.c_[input_feature_test_arr, np.array(dependent_feature_test_df)]
            
            logging.info('Saving preprocessor object')
            save_obj(
                file_path = self.datatransformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )             
            
            logging.info('Data transformation completed')
            return (train_arr, test_arr)
        except Exception as e:
            logging.info('!!! Error occured in data transformation')
            raise CustomException(e, sys)
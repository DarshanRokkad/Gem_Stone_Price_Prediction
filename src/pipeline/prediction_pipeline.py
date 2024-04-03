import os
import sys
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_obj
from dataclasses import dataclass

class CustomData:
    def __init__(
        self, 
        carat:float,
        depth:float,
        table:float,
        x:float,
        y:float,
        z:float,
        cut:str,
        color:str,
        clarity:str
        ):
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat' : [self.carat],
                'depth' : [self.depth],
                'table' : [self.table],
                'x' : [self.x],
                'y' : [self.y],
                'z' : [self.z],
                'cut' : [self.cut],
                'color' : [self.color],
                'clarity' : [self.clarity]
                }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Converted input into dataframe')
            return df
        except Exception as e:
            logging.info('!!! Error occured in get_data_as_dataframe')
            raise CustomException(e,sys)

@dataclass
class PredictPipelineConfig:
    preprocessor_path:str = os.path.join('artifacts', 'preprocessor.pkl')
    model_path:str = os.path.join('artifacts', 'model.pkl')

class PredictPipeline:    
    def __init__(self):
        self.prediction_pipeline_config = PredictPipelineConfig()
    
    def predict(self, features):
        try: 
            logging.info('Prediction pipeline started')

            preprocessor = load_obj(file_path = self.prediction_pipeline_config.preprocessor_path)
            model = load_obj(file_path = self.prediction_pipeline_config.model_path)
            logging.info('Preprocessor object and model object successfully loaded')

            scaled_data = preprocessor.transform(features)
            logging.info(f'Scaled input data')

            prediction = model.predict(scaled_data)[0]
            logging.info(f'Predicted output is {prediction}')
            
            logging.info('Prediction pipeline completed')
            return round(prediction, 2)        
        except Exception as e:
            logging.info('!!! Error occured in prediction pipeline')
            raise CustomException(e, sys)


# for testing purpose
# if __name__ == '__main__':
#     custom_data_obj = CustomData(1.08,62.7,55.0,6.53,6.59,4.09,'Ideal','H','VS2')
#     df = custom_data_obj.get_data_as_dataframe()
#     prediction_obj = PredictPipeline()
#     print(prediction_obj.predict(df))
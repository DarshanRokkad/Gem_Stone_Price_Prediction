from __future__ import annotations
from textwrap import dedent
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.pipeline.training_pipeline import TrainingPipeline
import numpy as np

training_pipeline = TrainingPipeline()

with DAG(
    'gemstone_training_pipeline',
    default_args = {'retries' : 2},
    description = 'it is my training pipeline',
    schedule = '@weekly',
    start_date = pendulum.datetime(2024, 4, 4, tz = 'UTC'),
    catchup = False,
    tags = ['Machine_Learning', 'Regression', 'Gemstone']
) as dag:
    dag.doc_md = __doc__
    
    def data_ingestion(**kwargs):
        ti = kwargs['ti']
        train_data_path, test_data_path = training_pipeline.start_data_ingestion()
        ti.xcom_push('data_ingestion_artifact', {'train_data_path':train_data_path, 'test_data_path':test_data_path})     # xcom is cross communication
    data_ingestion_task = PythonOperator(
        task_id = 'data_ingestion',
        python_callable = data_ingestion
    )
    data_ingestion_task.doc_md = dedent(
        '''
        #### Ingestion task
        This task creates a train and test data file.
        '''
    )
    
    
    def data_transformation(**kwargs):
        ti = kwargs['ti']
        data_ingestion_artifact = ti.xcom_pull(task_ids = 'data_ingestion', key = 'data_ingestion_artifact')
        train_arr, test_arr = training_pipeline.start_data_transformation(data_ingestion_artifact.train_data_path, data_ingestion_artifact.test_data_path)
        train_arr, test_arr = train_arr.tolist() , test_arr.tolist() 
        ti.xcom_push('data_transformation_artifact', {'train_arr':train_arr, 'test_arr':test_arr})
    data_transformation_task = PythonOperator(
        task_id = 'data_transformation',
        python_callable = data_transformation
    )
    data_transformation_task.doc_md = dedent(
        '''
        #### Transformation task
        This task performs the data transformation
        '''
    )
    
    
    def model_trainer(**kwargs):
        ti = kwargs['ti']
        data_transformation_artifact = ti.xcom_pull(task_id = 'data_transformation', key = 'data_transformation_artifact')
        train_arr = np.array(data_transformation_artifact['train_arr'])
        test_arr = np.array(data_transformation_artifact['test_arr'])
        training_pipeline.start_model_trainer(train_arr, test_arr)
    model_trainer_task = PythonOperator(
        task_id = 'model_trainer',
        python_callable = model_trainer
    )
    model_trainer_task.doc_md = dedent(
        '''
        #### Model trainer task
        This task perform training
        '''
    )
    
    
    # we have to config azure blob
    def push_data_to_azureblob(**kwargs):
        import os
        bucket_name = 'repository_name'
        artifact_folder = '/app/artifacts'
        # we can save it ti the azure blob
        # os.system(f"aws s3 sync {artifact_folder} s3:/{bucket_name}/artifact")
    push_data_to_azureblob_task = PythonOperator(
        task_id = 'push_data',
        python_callable = push_data_to_azureblob
    )
    push_data_to_azureblob_task.doc_md = dedent(
        '''
        #### Pushing data to azure blob task
        This task push data to the azure cloud
        '''
    )
    

data_ingestion_task >> data_transformation_task >> model_trainer_task >> push_data_to_azureblob_task
import os
from pathlib import Path

list_of_files = [
    
    'notebooks/experiments.ipynb',                      # folder for all jupyter notebooks
    
    'artifacts/.gitkeep',                               # folder to store csv and pickle files
    
    'requirements.txt',                                 # requirements for projects 
    'requirements_dev.txt',                             # requirements only development environment 
        
    'src/__init__.py',                                  # main source code folder
    'src/components/__init__.py',                       # components
    'src/components/01_data_ingestion.py',
    'src/components/02_data_transformation.py',
    'src/components/03_model_training.py',
    'src/components/04_model_evaluation.py',    
    'src/pipeline/__init__.py',                         # pipelines
    'src/pipeline/01_training_pipeline.py',
    'src/pipeline/02_prediction_pipeline.py',
    'src/exception.py',                                 # custom exception handling
    'src/logger.py',                                    # logging
    'src/utils.py',                                     # common functions
    
    'tests/unit/__init__.py',                            # folder for unit testing
    'tests/integration/__init__.py',                     # folder for integration testing
    
    'setup.py',                                         # for converting project into package 
    'setup.cfg',
    'init_setup.sh',
    'pyproject.toml',
    'tox.ini',                                          # to test the project in the local environment
    
    'application.py',                                   # for creating the flask application 
    'templates/index.html',                             # for creating the ui for the application
    'static/css/style.css',
    
    # deployment
    # '.ebextensions/python.config',                      # for deployment of machine learning model in aws elasitc beanstalk
    # 'Dockerfile'                                        # for containerizing the project
    
    '.github/workflows/main.yml',                        # github actions workflow for ci-cd pipeline  
    
    'images/.gitkeep',                                  # supporting images for github readme

]

# let's create the project structure
for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != '':
        os.makedirs(file_dir, exist_ok = True)
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass    # creating an empty file
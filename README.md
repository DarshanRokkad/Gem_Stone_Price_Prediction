<h1 align="center">:rocket: Gem Stone Price Prediction :rocket:</h1>

---

<h3 align="center">Problem Statement</h3>

Explain the problem statement

Dataset Link : [Regression with a Tabular Gemstone Price Dataset](https://www.kaggle.com/c/playground-series-s3e8/data)

---

<h3 align="center">Solution Explaination</h3>

Click the below image to see vedio solution explaination 

[![YouTube Video](images/youtube-tumbnail.png)](https://www.youtube.com/embed/______)

---

<h3 align="center">Approch for the problem</h3>

Explain the problem solving approch

---

<h3 align="center">Project UI</h3>

<p align="center"><img src="images/project-ui.png" width="700" height="400"></p>

---

<h3 align="center">API Testing Results</h3>

<p align="center"><img src="images/api-testing-results-screenshot.png" width="700" height="400"></p>

---

<h3 align="center">Project Structure</h3>

```
│  
├── .github
│   │
│   └── workflow                          
│       │
│       └── main.yml                         <-- contains yml code to create CI-CD pipeline for github actions
│  
├── artificats                               <-- Contains dataset(train, test and raw) and pickle files(preprocessor and model)
│  
├── images                                   <-- contains images used in readme file
│  
├── notebooks
│   │
│   └── experiment.ipynb                     <-- a jupyter notebook where eda and model training is performed
│  
├── resources                                <-- folder contains some usefull commands and steps used while build project 
│   
├── src
│   │
│   ├── components
│   │   │
│   │   ├── 01_data_ingestion.py             <-- module which reads data from different data source and do train test split
│   │   │                                        then save raw data, train data and test data inside artifact folder 
│   │   │
│   │   ├── 02_data_transformation.py        <-- module which takes training and test dataset and then do feature engineering
│   │   │                                        then save preprocessor as pickle file inside artifact folder 
│   │   │
│   │   ├── 03_model_training.py             <-- module which takes preprocessed training and test data and 
│   │   │                                        this data is used to train different models and selects best model 
│   │   │                                        it also perform hyperparameter tuning 
│   │   │
│   │   │
│   │   └── 04_model_evaluation.py           <-- module which calculate the performance metrics
│   │
│   ├── pipeline
│   │   │
│   │   ├── __init__.py
│   │   │
│   │   ├── 01_training_pipeline.py          <-- module used to train the model using training components
│   │   │
│   │   └── 02_prediction_pipeline.py        <-- module takes the input data given by user through flask web application and returns the prediction
│   │
│   ├── __init__.py
│   │
│   ├── exception.py                         <-- module to display the custom exception
│   │
│   ├── logger.py                            <-- module to create log folder for each execution and log the events whenever required.
│   │
│   └── utils.py                             <-- module to which contians functions that are commonly used.
│   
├── static
│   │
│   └── css                                  <-- contains all css files
│   
├── templates                                <-- contains all html files
│   
├── tests
│   │
│   ├── integration                          <-- folder contains module used to do integration testing
│   │
│   └── unit                                 <-- folder contains module used to do unit or module testing
│
├── .gitignore                               <-- used to ignore the unwanted file and folders
│
├── application.py                           <-- flask web application to take input from user and render output
│
├── init_setup.sh                            <-- file is likely a shell script used to initailize the setup
│
├── LICENSE                                  <-- copyright license for the github repository 
│
├── pyproject.toml                           <-- used to specify various project metadata and configuration settings
│
├── README.md                                <-- used to display the information about the project
│
├── requirements_dev.txt                     <-- text file which contain the dependencies in development environment
│
├── requirements.txt                         <-- text file which contain the dependencies/packages used in project 
│
├── setup.cfg                                <-- configuration file used to provide various settings related to packaging and distribution
│
├── setup.py                                 <-- python script used for building python packages of the project
│
├── template.py                              <-- program used to create the project structure
│
└── tox.ini                                  <-- used to automate and manage the testing of a project across multiple python environments
```

---

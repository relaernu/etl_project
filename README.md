# project_2
Bootcampspot Project 2

# Notebooks folder contains all the python codes

1. Before running any codes, just make sure the project folder structure is like:

    repo_root
    │
    ├── notebooks
    │   ├── 01_xxx -- notebook files
    │   ├── 02_xxx 
    │   ├── 03_xxx
    │   └── xxx.py -- python files
    │   
    ├── resources
    │   ├── xxx.tsv -- dataset files
    │   ├── xxx.csv  
    │   └── xxx.sqlite
    │
    ├─kaggle.json -- api username and key (*necessary)
    ├─dblogin.json -- database connection info (*necessary)
    └─README.md -- this file

2. In your python environment(PythonData for me), run following command to install kaggle api lib:
    pip install kaggle

3. Get your kaggle.json file for api key from kaggle.com ——> account ——> Create New API Token and put it as the structure shows

4. dblogin.json format as follow:
    {
        "username" : "xxxx",
        "password" : "xxxx",
        "database" : "xxxx"
    }


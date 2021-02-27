# Netflix or Disney+ and chill (ETL-Project)


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
    ├── Flask
    │   ├── app.py
    │   ├── myfunc.py
    │   ├── kaggle.py       
    │   ├── dblogin.json  
    │   └── kaggle.json
    │
    ├── SQL
    │   ├── <xxx>.sql 
    │   ├── <xxx>.sql
    │   ├── <xxx>.sql    
    │   ├── <xxx>.sql 
    │   └── <xxx>.sql
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

5. In postgresql, create a database call "movies"

6. For flask solution, run the app.py, then you can use the following link to finish the work:
    1) "/download?src=<imdb|kaggle>" or "/download" to download the data from imdb or kaggle or both of them to "./resources" folder
    2) "/unzip" after downloading the data, unzip them to get the csv/tsv file
    3) "/loaddata?src=<imdb|kaggle>" or "/loaddata" after unzipping the file, clean them up, load them into postgresql

7. For SQL folder, there are some transformation 
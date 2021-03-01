# Netflix or Disney+ and chill (ETL-Project)
# Notebooks folder contains all the python codes

1. Folder structure

──repo_root
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
    │   ├── xxx.zip -- downloaded zip file
    │   └── xxx.gz -- downloaded gzip file  
    │
    ├── Flask
    │   ├── app.py
    │   ├── myfunc.py
    │   ├── kaggle.py       
    │   ├── dblogin.json  -- database connection info (*necessary for using Flask to run)
    │   └── kaggle.json   -- api username and key (*necessary for using Flask to run)
    │
    ├── SQL
    │   ├── 1_UnionTable.sql 
    │   ├── <xxx>.sql
    │   ├── <xxx>.sql    
    │   ├── <xxx>.sql 
    │   └── <xxx>.sql
    │
    ├─kaggle.json -- api username and key (*necessary for using jupyter notebook to run)
    ├─dblogin.json -- database connection info (*necessary for using jupyter notebook to run)
    └─README.md -- this file

2. Make sure all the dependent librarise had been installed

3. In your python environment(PythonData for me), run following command to install kaggle api lib:
    pip install kaggle

4. Get your kaggle.json file for api key from kaggle.com ——> account ——> Create New API Token and put it where as the structure shows

5. put dblogin.json format as follow to where the structure shows:
    {
        "username" : "xxxx",
        "password" : "xxxx",
        "database" : "xxxx"
    }

6. In postgresql, create a database call "movies"

7. For flask solution, run the app.py, then you can use the following link to finish the work:
    1) "/" to home page
    2) "/download?src=<imdb|kaggle>" or "/download" to download the data from imdb or kaggle or both of them to "./resources" folder
    3) "/unzip" after downloading the data, unzip them to get the csv/tsv file
    4) "/loaddata?src=<imdb|kaggle>" or "/loaddata" after unzipping the file, clean them up, load them into postgresql

8. For SQL folder, there are some query and transformation of the datas
    1) run 1_UnionTable.sql to creat agerated table, and union the Netflix table and Disney+ tables to a new table call NetflixDisney
    2) run 2_Split_Country_Director.sql to split the country and director column array values to new tables movie_country and movie_director
    3) there are some query in 3_Join_Table.sql to do some search
    4) 10_OtherOperation.sql for some test query

9. We have made a simple html for the project to be run easily:
    1) in Flask folder, run "python app.py"
    2) browser "http://127.0.0.1:5000" in your browser
    3) at the "Preparation" part, we can download -> unzip -> load data to database
    4) at the "E.T.L." part, we can download the ETL & ERD diagram
    5) at the "Documention" part, we can download the README.md and report.docx
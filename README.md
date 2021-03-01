## Netflix or Disney+ and Chill? (ETL-Project)

![disney&netflix](https://cdn.wccftech.com/wp-content/uploads/2020/02/netvsdis-1024x614-1.jpg)

#### -- Project Status: [Completed]

### Project Intro/Objective

The purpose of this project is to create a database of movies where users can search for a movie and all its information, and determine if it is available on Netflix or Disney+.

### The Extraction

The 2 datasets we have used are [Netflix](https://www.kaggle.com/shivamb/netflix-shows) and [Disney+](https://www.kaggle.com/unanimad/disney-plus-shows) which were sourced from Kaggle. In addition, we incorporated them with the dataset of [IMDB](https://www.imdb.com/interfaces/) to standardise the rating for all movies and create our database to help users search for movies (e.g. by title or region) that are readily available on either streaming platform. 

### The Transformation

As some movies are directed by more than one director, we cleaned up the data by 
separating a list of directors’ names from the provided data. Similarly, we did the same for a list of movie regions as some movies can be viewed in more than one region. We used jupyter notebooks for testing and also used python script to create a flask solution to serve it. Once the data cleaning had been completed, we merged the datasets by using SQL. 

### The Data Storage

This project used a relational database to store the data.

### Instructions  

For the codes to run properly, there are several steps to be taken.
Please follow the steps below:

1. Open gitbash/terminal and run “conda activate PythonData”.
2. Next, run “pip install kaggle”.
3. Then, run “pip install psycopg2”.
4. Sign in or register for an account on https://www.kaggle.com/ to get your kaggle.json file for the API key. 
Once you are in your account, go to “Account” and click on “Create New API Token”. 

![Alt text](images/kaggle.png?raw=true "Kaggle")

![Alt text](images/account.png?raw=true "Account")

![Alt text](images/api.png?raw=true "API")

5. Git pull the project folder and add the downloaded kaggle.json file to the folder.

![Alt text](images/root.png?raw=true "root")

6. Create a dblogin.json file and include the following information with your PostgreSQL username and password.  Save it to the project folder. 
    {
        "username" : "XXXX",
        "password" : "XXXX",
        "database": "movies"
    }

![Alt text](images/root2.png?raw=true "root")

7. In PostgreSQL, create a database and name it “movies”. 

![Alt text](images/postgresql.png?raw=true "PostgreSQL")

Option 1: via Jupyter Notebook: 
1. Run jupyter notebooks in the following order:  “01_Prepare_Files.ipynb”, “02_Load_IMDB_data”, “03_Load_Kaggle_Data”. The extracted files will be saved in the “resources” folder in the project folder. 

![Alt text](images/resources.png?raw=true "Resources")

Option 2: via Flask solution: 
1. Add kaggle.json and dblogin.json files to the “Flask” folder in the project folder. 

![Alt text](images/flask.png?raw=true "Flask")

2. Run app.py.

![Alt text](images/flaskresources.png?raw=true "Resources")

3. Run http://127.0.0.1:5000/download?src=imdb, http://127.0.0.1:5000/download?src=kaggle or http://127.0.0.1:5000/download to download the data from IMDB, kaggle or both, and they will be saved to ..\Flask\resources.
4. To unzip the downloaded data, run http://127.0.0.1:5000/unzip to extract the CSV/TSV files.

5. After cleaning the extracted data, run http://127.0.0.1:5000/loaddata?src=imdb, http://127.0.0.1:5000/loaddata?src=kaggle 
or http://127.0.0.1:5000/loaddata to load the IMDB, Kaggle or both datasets into PostgreSQL.


Option 3: via HTML
1. Add kaggle.json and dblogin.json files to the “Flask” folder in the project folder. 

![Alt text](images/flask.png?raw=true "Flask")

2. Run app.py.
3. Run http://127.0.0.1:5000/
3. Under the Download Data section, click on the unique links to download the data from IMDB, Kaggle or both, and they will be saved to ..\Flask\resources. 

![Alt text](images/datapreparation.png?raw=true "Preparation")

4. Under the Unzip Files section, click on the unique link to unzip and extract the CSV/TSV files from the downloaded files.

5. Under the Clean and Load Data section, click on the unique links after cleaning the extracted data to load the IMDB, Kaggle or both datasets into PostgreSQL.

6. To download the ETL & ERD diagram, click on the unique links under the EXTRACTION|TRANSFORMATION|LOADING section.

![Alt text](images/ETL.png?raw=true "ETL")

7. To download the README.md and report.docx, click on the unique links under the DOCUMENTATION section.

![Alt text](images/documentation.png?raw=true "Documentation")



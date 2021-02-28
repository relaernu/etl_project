## Netflix or Disney+ and Chill? (ETL-Project)

![disney&netflix](https://cdn.wccftech.com/wp-content/uploads/2020/02/netvsdis-1024x614-1.jpg)

#### -- Project Status: [Completed]

### Project Intro/Objective

The purpose of this project is to create a database of movies where users can search for a movie and all its information, and determine if it is available on Netflix or Disney+

### The Extraction

The 2 datasets we have used are [Netflix](https://www.kaggle.com/shivamb/netflix-shows) and [Disney+](https://www.kaggle.com/unanimad/disney-plus-shows) which were sourced from Kaggle. In addition, we incorporated them with the dataset of [IMDB](https://www.imdb.com/interfaces/) to standardise the rating for all movies and create our database to help users search for movies (e.g. by title or region) that are readily available on either streaming platform.

### The Transformation

As some movies are directed by more than one director, we cleaned up the data by
separating a list of directors’ names from the provided data. Similarly, we did the same for a list of movie regions as some movies can be viewed in more than one region. We used jupyter notebooks for testing and once the data cleaning was completed, we merged the datasets by using SQL. We also used python script in flask to find movies and their information from the Netflix and Disney+ datasets.

### The Data Storage

This project used a relational database to store the data.

### Instruction

For the codes to run properly, there are several steps to be taken.
Please follow the steps below:

1. Open gitbash/terminal and run “conda activate PythonData”.
2. Next, run “pip install kaggle”.
3. Then, run “pip install psycopg2”.
4. Sign in or register for an account on kaggle.com to get your kaggle.json file for API key. Once you are in your account, go to “Account” and click on “Create New API Token”.
5. Gitpull the project folder and add the downloaded kaggle.json file to the folder as shown in the screenshot.
6. Create a dblogin.json file and include the following information with your PostgreSQL username and password: { username: “XXXX”, password: “XXXX”, database: “movies”}. Save it to the project folder as shown in the screenshot.
7. In PostgreSQL, create a database and name it “movies”.
8. Run jupyter notebooks in the following order: “01_Prepare_Files.ipynb”, “02_Load_IMDB_data”, “03_Load_Kaggle_Data”. The extracted files will be saved in the “resources” folder in the project folder.

### Flask soluction

1. Add kaggle.json and dblogin.json files to the “Flask” folder in the project folder.
2. Run app.py.
3. To download the data, run http://127.0.0.1:5000/download and data will be downloaded to the ..\Flask\resources folder.
4. To unzip the downloaded data, run http://127.0.0.1:5000/unzip to extract the CSV/TSV files.
5. After cleaning the extracted data, run http://127.0.0.1:5000/loaddata?src=imdb and http://127.0.0.1:5000/loaddata?src=kaggle to load them into PostgreSQL.

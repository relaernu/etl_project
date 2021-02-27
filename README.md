## Netflix or Disney+ and Chill? (ETL-Project)

![disney&netflix](https://cdn.wccftech.com/wp-content/uploads/2020/02/netvsdis-1024x614-1.jpg)

#### -- Project Status: [Completed]

### Project Intro/Objective

The purpose of this project is to create a database of movies where we can search the title and all the information regarding the movie will show up. By seaching through our data base wwe can also look up with platform the movie is available on whether it is Netflix or Disney+.

### The Extraction

The 2 datasets we use are [Netflix](https://www.kaggle.com/shivamb/netflix-shows) and [Disney+](https://www.kaggle.com/unanimad/disney-plus-shows) which were derived from Kaggle. We also used [IMDB](https://www.imdb.com/interfaces/) to create database for other people to search movie base on the title or region to see whether it is readily available for them and which platform it is on

### The Transformation

We cleaned up the data by separating the directors for the movies with multiple directors and the regions as well. Once we completed the cleaning we merge the datasets and these 2 steps were completed using SQL. The filtering was completed by using jupyter notebook and python script in flask in order to find the movies and information from the datasets for the 2 streaming platforms.

### The Data Storage

This project will use relational database to store the data

### Instruction

For the code to run properly there are several steps to be taken
Please follow the steps below

1. pip install kaggle
2. pip install psycopg2
3. Get your kaggle.json file for api key form kaggle.com
4. Sign in or register an account
5. Once you have opened an account, create an api token

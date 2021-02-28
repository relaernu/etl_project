import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
import json

def loadimdb(file_folder):
    title_file = os.path.join(file_folder,"title.tsv")
    rating_file = os.path.join(file_folder,"rating.tsv")
    crew_file = os.path.join(file_folder,"crew.tsv")
    name_file = os.path.join(file_folder,"name.tsv")

    df_title = pd.read_csv(title_file, sep="\t")
    df_rating = pd.read_csv(rating_file, sep="\t")
    df_crew = pd.read_csv(crew_file, sep="\t")
    df_name = pd.read_csv(name_file, sep="\t")

    # clean up title
    df_title_movie = df_title.loc[df_title["titleType"] == "movie"]
    df_title_final = df_title_movie[["tconst", "primaryTitle", "originalTitle", "startYear"]]
    df_title_final.columns = ["ID", "PrimaryTitle", "OriginalTitle", "ReleaseYear"]
    df_title_final = df_title_final.replace("\\N", np.NaN)
    df_title_final = df_title_final.reset_index(drop=True)
    # df_title_final["ID"] = df_title_final["ID"].str.strip("t")
    # df_title_final["ID"] = df_title_final["ID"].astype(int)
    df_title_final["ReleaseYear"] = df_title_final["ReleaseYear"].fillna(0)
    df_title_final["ReleaseYear"] = df_title_final["ReleaseYear"].astype(int)

    # clean up rating
    df_rating_final = df_rating.copy()
    df_rating_final.columns = ["ID", "AverageRating", "Votes"]

    # clean up crew
    df_crew_final = df_crew.copy()
    df_crew_final.columns = ["ID", "Directors", "Writers"]
    df_crew_final = df_crew_final.replace("\\N", np.NaN)

    #clean up name
    df_name_final = df_name[["nconst","primaryName"]]
    df_name_final.columns = ["ID", "Name"]

    # merge title with rating
    df_merge = df_title_final.merge(df_rating_final, on=["ID"], how="left")

    # then merge with crew
    df_merge = df_merge.merge(df_crew_final, on=["ID"], how="left")

    # set "ID" as index
    df_merge = df_merge.set_index("ID")

    # the data in column "Directors" will have multiple values, so split row to 1 to 1 mapping
    df_title_name = df_merge[["Directors"]]
    df_title_name["Directors"] = df_title_name["Directors"].str.split(",")
    stack = df_title_name["Directors"].apply(pd.Series).stack()
    df_stack = pd.DataFrame(stack)
    df_stack = df_stack.reset_index()
    df_stack = df_stack.drop('level_1', axis=1)
    df_stack.columns = ["ID", "Director"]
    # replace the Director ID with Director Name
    df_stack_merge = df_stack.merge(df_name_final, left_on=["Director"], right_on=["ID"])
    df_title_director = df_stack_merge[["ID_x", "Name"]]
    df_title_director.columns = ["ID", "Director"]
    df_title_director.set_index("ID", inplace=True)

    # load data to postsql
    with open("../dblogin.json") as json_file:
        login = json.load(json_file)
    json_file.close()
    engine = create_engine(f'postgresql://{login["username"]}:{login["password"]}@localhost/{login["database"]}')

    # create or recreate table
    df_merge.to_sql("IMDB", engine, if_exists="replace")
    engine.execute('ALTER TABLE "IMDB" ADD PRIMARY KEY ("ID");')

    df_title_director.to_sql("IMDB_Director", engine, if_exists="replace")

    return {
        "files" : [title_file, rating_file, crew_file, name_file],
        "tables" : ["IMDB","IMDB_Director"]
    }

def loadkaggle(file_folder):
    # files paths
    disney_file = os.path.join(file_folder, "disney_plus_shows.csv")
    netflix_file = os.path.join(file_folder, "netflix_titles.csv")
    # multi_file = os.path.join(file_folder, "MoviesOnStreamingPlatforms_updated.csv")

    df_disney = pd.read_csv(disney_file)
    df_netflix = pd.read_csv(netflix_file)
    # df_multi = pd.read_csv(multi_file)

    # clean up disney dataframe
    df_disney_clean = df_disney[["imdb_id", "title", "type", "rated", "year", "director", "country"]]

    # filter 
    df_disney_clean = df_disney_clean.loc[df_disney_clean["type"] == "movie"]
    df_disney_clean.columns = ["ID", "Title", "Type", "Rated", "ReleaseYear", "Director", "Country"]
    #df_disney_clean["ID"] = df_disney_clean["ID"].str.strip("t")
    #df_disney_clean["ID"] = df_disney_clean["ID"].astype(int)
    df_disney_clean["ReleaseYear"] = df_disney_clean["ReleaseYear"].fillna(0)
    df_disney_clean["ReleaseYear"] = df_disney_clean["ReleaseYear"].astype(int)
    df_disney_clean = df_disney_clean.set_index("ID")

    # cleanup netflix
    df_netflix_clean = df_netflix[["show_id", "type", "title", "director", "country", "release_year", "rating"]]
    df_netflix_clean = df_netflix_clean.loc[df_netflix_clean["type"] == "Movie"]
    df_netflix_clean.columns = ["n_ID", "Type", "Title", "Director", "Country", "ReleaseYear", "Rating"]
    #df_netflix_clean["n_ID"] = df_netflix_clean["n_ID"].str.strip("s")
    #df_netflix_clean["n_ID"] = df_netflix_clean["n_ID"].astype(int)
    df_netflix_clean = df_netflix_clean.set_index("n_ID")

    # "Director" column include multiple values, split them to 1:1 row
    df_netflix_director = df_netflix_clean[["Title", "Director"]]
    #df_netflix_director.fillna("N/A", inplace=True)
    df_netflix_director.reset_index(inplace=True)
    df_netflix_director.set_index(["n_ID", "Title"], inplace=True)
    
    # clean up the multi platform data
    # df_multi_clean = df_multi[["ID", "Title", "Year", "Age", "IMDb", "Netflix", "Disney+", "Type", "Directors", "Country"]]
    # df_multi_clean.columns = ["m_ID", "Title", "Year", "Age", "IMDB", "Netflix", "DisneyPlus", "Type", "Directors", "Country"]
    # df_multi_clean = df_multi_clean.set_index("m_ID")

    # load data into postgresql
    with open("../dblogin.json") as json_file:
        login = json.load(json_file)
    json_file.close()
    engine = create_engine(f'postgresql://{login["username"]}:{login["password"]}@localhost/{login["database"]}')
    
    # Load disney and set primary key
    df_disney_clean.to_sql("DisneyPlus", engine, if_exists="replace")
    engine.execute('ALTER TABLE "DisneyPlus" ADD PRIMARY KEY ("ID");')

    # Load Netflix and set primary key
    df_netflix_clean.to_sql("Netflix", engine, if_exists="replace")
    engine.execute('ALTER TABLE "Netflix" ADD PRIMARY KEY ("n_ID");')

    # Load multi platform and set primary key
    # df_multi_clean.to_sql("Multiplatform", engine, if_exists="replace")
    # engine.execute('ALTER TABLE "Multiplatform" ADD PRIMARY KEY ("m_ID");')

    return {
#        "files" : [disney_file, netflix_file, multi_file],
        "files" : [disney_file, netflix_file],
        "tables" : ["DisneyPlus", "Netflix"]
    }
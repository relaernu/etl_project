from urllib import request
import os
import time

from kaggle.api.kaggle_api_extended import KaggleApi
import json

from zipfile import ZipFile
import gzip

def KaggleDownloadApi(download_dict):

    # download dict should contain the following keys:
    # 
    #   "key" : api key from kaggle
    #   "username" : api username from kaggle
    #   "url" : the project url as http://kaggle.com/<user>/<project>
    #   "file" : kaggle file name
    #   "folder" : output folder
    #
    # will return true if successfully downloaded

    api = KaggleApi()
    api.set_config_value("key", download_dict["key"], quiet=True)
    api.set_config_value("username", download_dict["username"], quiet=True)
    api.authenticate()

    urls = download_dict["url"].split("/")
    dataset = urls[-2] + "/" + urls[-1]

    result = api.dataset_download_file(dataset, download_dict["file"], download_dict["folder"], force=True, quiet=True)

    return result

def kaggledownload(download_folder):
    downloaded = False
    downloadfiles = []

    if not os.path.exists(download_folder):
        os.mkdir(download_folder)

    with open("kaggle.json") as json_file:
        kaggle_secret = json.load(json_file)

        # disney+ data at https://www.kaggle.com/unanimad/disney-plus-shows
        ddict = {
            "key" : kaggle_secret["key"],
            "username" : kaggle_secret["username"],
            "url" : "https://www.kaggle.com/unanimad/disney-plus-shows",
            "file" : "disney_plus_shows.csv",
            "folder" : download_folder
        }
        while not downloaded:
            try:
                downloaded = KaggleDownloadApi(ddict)
                downloadfiles.append(os.path.join(download_folder, ddict["file"]))
            except:
                time.sleep(5)
        
        # netflix data at https://www.kaggle.com/shivamb/netflix-shows
        downloaded = False
        ddict["url"] = "https://www.kaggle.com/shivamb/netflix-shows"
        ddict["file"] = "netflix_titles.csv"

        while not downloaded:
            try:
                downloaded = KaggleDownloadApi(ddict)
                downloadfiles.append(os.path.join(download_folder, ddict["file"]))
            except:
                time.sleep(5)

        # all stream platform data at https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney
        downloaded = False
        ddict["url"] = "https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney"
        ddict["file"] = "MoviesOnStreamingPlatforms_updated.csv"

        while not downloaded:
            try:
                downloaded = KaggleDownloadApi(ddict)
                downloadfiles.append(os.path.join(download_folder, ddict["file"]))
            except:
                time.sleep(5)

        return downloadfiles

def imdbdonwload(download_folder):

    downloadfiles = []

    url_title = "https://datasets.imdbws.com/title.basics.tsv.gz"
    url_rating = "https://datasets.imdbws.com/title.ratings.tsv.gz"
    url_crew = "https://datasets.imdbws.com/title.crew.tsv.gz"
    url_name = "https://datasets.imdbws.com/name.basics.tsv.gz"

    downloaded = False

    if not os.path.exists(download_folder):
        os.mkdir(download_folder)

    # download title
    while not downloaded:
        try:
            file, msg = request.urlretrieve(url_title, os.path.join(download_folder, "title.tsv.gz"))
            downloaded = True
            downloadfiles.append(file)
        except:
        # if download fails, restart it after 5 sec
            time.sleep(5)
    
    downloaded = False
    # download rating
    while not downloaded:
        try:
            file, msg = request.urlretrieve(url_rating, os.path.join(download_folder, "rating.tsv.gz"))
            downloaded = True
            downloadfiles.append(file)
        except:
        # if download fails, restart it after 5 sec
            time.sleep(5)
    
    downloaded = False
    # download crew
    while not downloaded:
        try:
            file, msg = request.urlretrieve(url_crew, os.path.join(download_folder, "crew.tsv.gz"))
            downloaded = True
            downloadfiles.append(file)
        except:
        # if download fails, restart it after 5 sec
            time.sleep(5)

    downloaded = False
    # download crew
    while not downloaded:
        try:
            file, msg = request.urlretrieve(url_name, os.path.join(download_folder, "name.tsv.gz"))
            downloaded = True
            downloadfiles.append(file)
        except:
        # if download fails, restart it after 5 sec
            time.sleep(5)

    return downloadfiles

def unzipfiles(folder):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    outlist = []
    for file in files:
#    print(file)
        filename, ext = os.path.splitext(file)
        if ext == ".gz":
            #c_name, c_ext = os.path.splitext(filename)
            input_file = gzip.GzipFile(os.path.join(folder, file), 'rb')
            s = input_file.read()
            input_file.close()
            output = open(os.path.join(folder, filename), 'wb')
            output.write(s)
            output.close()
            outlist.append({
                "from" : os.path.join(folder, file),
                "to" : os.path.join(folder, filename)
            })
        elif ext == ".zip":
            with ZipFile(os.path.join(folder, file), "r") as zip_file:
               zip_file.extractall(folder)
            outlist.append({
                "zip" : os.path.join(folder, file)
            })
    return outlist




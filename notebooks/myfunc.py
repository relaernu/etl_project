from kaggle.api.kaggle_api_extended import KaggleApi

# download dict should contain the following keys:
# 
#   "key" : api key from kaggle
#   "username" : api username from kaggle
#   "url" : the project url as http://kaggle.com/<user>/<project>
#   "file" : kaggle file name
#   "folder" : output folder
#
# will return true if successfully downloaded

def KaggleDownload(download_dict):
    api = KaggleApi()
    api.set_config_value("key", download_dict["key"], quiet=True)
    api.set_config_value("username", download_dict["username"], quiet=True)
    api.authenticate()

    urls = download_dict["url"].split("/")
    dataset = urls[-2] + "/" + urls[-1]

    result = api.dataset_download_file(dataset, download_dict["file"], download_dict["folder"], force=True, quiet=True)

    return result



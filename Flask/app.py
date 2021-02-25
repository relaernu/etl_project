from flask import Flask, request, jsonify
import myfunc
import loaddata
import json

app = Flask(__name__)

download_path = "resources"
files = []

@app.route("/download")
def download():
    downsrc = request.args.get("src")
    if downsrc == "imdb":
        files = myfunc.imdbdonwload(download_path)
    elif downsrc == "kaggle":
        files = myfunc.kaggledownload(download_path)
    return jsonify(files)

@app.route("/unzip")
def unzip():
    files = myfunc.unzipfiles(download_path)
    return jsonify(files)

@app.route("/loaddata")
def load():
    result = {}
    param = request.args.get("src")
    if param == "imdb":
        result = loaddata.loadimdb(download_path)
    elif param == "kaggle":
        result = loaddata.loadkaggle(download_path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
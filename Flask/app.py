from flask import Flask, request, jsonify, render_template
import myfunc
import loaddata
import json

app = Flask(__name__)

download_path = "resources"
files = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download():
    downsrc = request.args.get("src")
    if downsrc == "imdb":
        files = myfunc.imdbdonwload(download_path)
    elif downsrc == "kaggle":
        files = myfunc.kaggledownload(download_path)
    elif downsrc is None:
        files = myfunc.imdbdonwload(download_path)
        files.extend(myfunc.kaggledownload(download_path))
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
    elif param is None:
        result = loaddata.loadimdb(download_path)
        result2 = loaddata.loadkaggle(download_path)
        result["files"].extend(result2["files"])
        result["tables"].extend(result2["tables"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
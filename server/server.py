from flask import Flask, jsonify, render_template, request, send_file,  after_this_request
import os
import subprocess
from pathlib import Path
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file=request.files["book"]
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    name = file.filename
    ext = Path(name).suffix
    if ext == ".epub" :
        subprocess.run([os.path.join(BASE_DIR, "kindlegen"),os.path.join(UPLOAD_FOLDER, name)])
        os.remove(os.path.join(UPLOAD_FOLDER, name))
    if ext == ".fb2" :
        subprocess.run(["zip" , os.path.join(UPLOAD_FOLDER, name+".zip"), os.path.join(UPLOAD_FOLDER, name)])
        os.remove(os.path.join(UPLOAD_FOLDER, name))
        subprocess.run([os.path.join(BASE_DIR, "kindlegen"), os.path.join(UPLOAD_FOLDER, name+".zip")])
        os.remove(os.path.join(UPLOAD_FOLDER, name+".zip"))
    return "SAVED"
@app.route("/download/<filename>")
def download(filename):
    @after_this_request
    def delete(response):
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        return response
    return send_file(os.path.join(UPLOAD_FOLDER, filename))
@app.route("/list")
def list():
    return jsonify(os.listdir(UPLOAD_FOLDER))

app.run(host="0.0.0.0", port=3000, debug=True)

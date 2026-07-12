from flask import Flask, jsonify, render_template, request, send_file,  after_this_request, redirect
import os
import subprocess
from pathlib import Path
app = Flask(__name__)
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new")
def new():
    c = random.randint(1000, 9999)
    pinfolder= os.path.join(UPLOAD_FOLDER, str(c))
    os.makedirs(pinfolder)
    return str(c)

@app.route("/pair", methods=["POST"])
def pair():
    pin=request.form["pin"]
    pinfolder= os.path.join(UPLOAD_FOLDER,pin)
    if os.path.isdir(pinfolder):
        return redirect("/" + pin)
    else:
        return "invalid pin"

@app.route("/<pin>")
def page(pin):
    pinfolder = os.path.join(UPLOAD_FOLDER,pin)
    if os.path.isdir(pinfolder):
        return render_template("page.html")
    else:
        return "invalid code"
@app.route("/<pin>/upload", methods=["POST"])
def upload(pin):
    file=request.files["book"]
    pinfolder = os.path.join(UPLOAD_FOLDER,pin)
    file.save(os.path.join(pinfolder, file.filename))
    name = file.filename
    ext = Path(name).suffix
    if ext == ".epub" :
        subprocess.run([os.path.join(BASE_DIR, "kindlegen"),os.path.join(pinfolder, name)])
        os.remove(os.path.join(pinfolder, name))
    if ext == ".fb2" :
        subprocess.run(["zip" , os.path.join(pinfolder, name+".zip"), os.path.join(pinfolder, name)])
        os.remove(os.path.join(pinfolder, name))
        subprocess.run([os.path.join(BASE_DIR, "kindlegen"), os.path.join(pinfolder, name+".zip")])
        os.remove(os.path.join(pinfolder, name+".zip"))
    return "SAVED"
@app.route("/<pin>/download/<filename>")
def download(pin, filename):
    pinfolder = os.path.join(UPLOAD_FOLDER,pin)
    @after_this_request
    def delete(response):
        os.remove(os.path.join(pinfolder, filename))
        return response
    return send_file(os.path.join(pinfolder, filename))
@app.route("<pin>/list")
def list(pin):
    pinfolder = os.path.join(UPLOAD_FOLDER,pin)
    return jsonify(os.listdir(pinfolder))

app.run(host="0.0.0.0", port=3000, debug=True)

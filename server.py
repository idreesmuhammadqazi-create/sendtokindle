from flask import Flask, jsonify, render_template, request, send_file
import os
app = Flask(__name__)
UPLOAD_FOLDER="uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file=request.files["book"]
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return "SAVED"


app.run(host="0.0.0.0", port=3000, debug=True)

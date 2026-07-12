import os
import requests
import subprocess
pin = ""
BASE_DIR = "/mnt/us"
documents = os.path.join(BASE_DIR, "documents")
with open("code.txt") as t:
    pin = t.read()
    

booklist = requests.get("https://idrees.hackclub.app/"+pin+"/list").json()
subprocess.run(["eips", "15" , "10", "got book list"])
subprocess.run(["eips", "15" , "12", str(booklist)])

if booklist:
    filename = booklist[0]
    book = requests.get("https://idrees.hackclub.app/"+pin+"/download/"+filename).content

    with open(os.path.join(documents, filename), "wb") as text:
        text.write(book)
        subprocess.run(["eips", "15" , "13", f"got {filename}"])
else:
    subprocess.run(["eips", "15" , "13", "no books"])

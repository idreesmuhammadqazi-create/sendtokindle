import os
import requests
pin = ""
BASE_DIR = "/mnt/us"
documents = os.path.join(BASE_DIR, "documents")
with open("code.txt") as t:
    pin = t.read()
    

booklist = requests.get("http://192.168.100.28:3000/"+pin+"/list").json()
print("got book list")
print(booklist)

if booklist:
    filename = booklist[0]
    book = requests.get("http://192.168.100.28:3000/"+pin+"/download/"+filename).content

    with open(os.path.join(documents, filename), "wb") as text:
        text.write(book)
        print("done", filename)
else:
    print("no books")
import os
import time
import requests
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
documents = os.path.join(BASE_DIR, "documents")

os.makedirs(documents, exist_ok=True)
while '1' == '1' :
    booklist = requests.get("http://0.0.0.0:3000/list").json()
    print("got book list")
    print(booklist)
    if booklist:
        filename=booklist[0]
        book=requests.get(f"http://0.0.0.0:3000/download/{filename}").content
        with open(os.path.join(documents ,filename), "wb") as text:
            text.write(book)
        print("done ", filename)
    time.sleep(5)
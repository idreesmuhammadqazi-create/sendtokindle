import os
import requests

BASE_DIR = "/mnt/us"
documents = os.path.join(BASE_DIR, "documents")

booklist = requests.get("http://192.168.100.28:3000/list").json()
print("got book list")
print(booklist)

if booklist:
    filename = booklist[0]
    book = requests.get(f"http://192.168.100.28:3000/download/{filename}").content

    with open(os.path.join(documents, filename), "wb") as text:
        text.write(book)
        print("done", filename)
else:
    print("no books")
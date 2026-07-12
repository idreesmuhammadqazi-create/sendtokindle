import requests
import subprocess
pin = requests.get("http://idrees.hackclub.app/new").text
with open("code.txt", "w") as t:
    t.write(pin)
print("YOUR PIN IS ",pin )
subprocess.run(["eips", "25" , "18", "your pin is"])
subprocess.run(["eips", "25" , "20", pin])
subprocess.run(["eips", "25" , "18", "your pin is"])
subprocess.run(["eips", "25" , "20", pin])
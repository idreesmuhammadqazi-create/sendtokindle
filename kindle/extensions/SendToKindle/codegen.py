import requests
import subprocess
pin = requests.get("http://192.168.100.28:3000/new").text
with open("code.txt", "w") as t:
    t.write(pin)
print("YOUR PIN IS ",pin )
subprocess.run(["eips", "25" , "18", "your pin is"])
subprocess.run(["eips", "25" , "20", pin])
subprocess.run(["eips", "25" , "18", "your pin is"])
subprocess.run(["eips", "25" , "20", pin])
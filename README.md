# Send To Kindle 
this is my project im doing to learn flask and to allow myself to send books to my kindle 4 
thing is amazon cut the send to kindle via email feature off and i want to recreate it 
the first version requires the file to be in the right format and the reciever.py that runs on the kindle is probably gonna take way too much battery 
the next thing ill do is to make a mail server for this so you can have a email address to mail ur books to again
after that ill add conversions and other stuff but mostly thats it 

right now   the current repo structure is :
```├── kindle
│   ├── documents
│   └── reciver.py
├── README.md
└── server
    ├── server.py
    ├── templates
    │   └── index.html
    └── uploads
```
for a quickstart do this 
```
1 JAILBREAK your kindle (Yes this is a must)
2 get PYTHON 3 for kindle (will add links later)
3 get KUAL this will be the luancher
4 run server.py
5 open localhost:3000
6 upload
7 run KUAL and select SEND TO KINDLE and then run it 
8 the book will appear
```

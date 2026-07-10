# Send To Kindle 
this is my project im doing to learn flask and to allow myself to send books to my kindle 4 
thing is amazon cut the send to kindle via email feature off and i want to recreate it 
the first version requires the file to be in the right format (epub or mobi)
the next thing ill do is to make a mail server for this so you can have a email address to mail ur books to again
after that ill add conversions and other stuff but mostly thats it 

right now   the current repo structure is :
```
.
├── kindle
│   └── extensions
│       └── SendToKindle
│           ├── bin
│           │   └── check.sh
│           ├── config.xml
│           ├── menu.json
│           └── receiver.py
├── LICENSE
├── README.md
└── server
    ├── epub2mobi.py
    ├── server.py
    ├── templates
    │   └── index.html
    └── uploads

```
for a quickstart do this 
```
1 JAILBREAK your kindle (Yes this is a must)
2 get PYTHON 3 for kindle (will add links later)
3 get mkk (mobileread kindle kit or something)
4 get KUAL this will be the launcher
5 connect your kindle to your pc and copy the extensions folder in the repo to kindle root folder that you see 
6 run server.py
7 open localhost:3000
8 upload
9 run KUAL and select SEND TO KINDLE and then run it 
10 the book will appear
```

```
links : https://www.mobileread.com/forums/showthread.php?t=225030
download kindle jailbreak , python 3 for kindle ,Mobileread Kindlet Kit ,KUAL
```
acknowledgements : this project now uses epub2mobi by hyle (MIT license)

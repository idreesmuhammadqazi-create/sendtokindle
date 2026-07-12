# Send To Kindle 
this is my project im doing to learn flask and to allow myself to send books to my kindle 4 
thing is amazon cut the send to kindle via email feature off and i want to recreate it 
the first version requires the file to be in the right format (epub or mobi or fb2)
the next thing ill do is to make a mail server for this so you can have a email address to mail ur books to again

right now   the current repo structure is :
```
.
├── kindle
│   └── extensions
│       └── SendToKindle
│           ├── bin
│           │   ├── check.sh
│           │   └── pin.sh
│           ├── codegen.py
│           ├── config.xml
│           ├── menu.json
│           └── receiver.py
├── LICENSE
├── README.md
└── server
    ├── kindlegen
    ├── server.py
    ├── templates
    │   ├── index.html
    │   └── page.html
    └── uploads


```
for a quickstart do this 
```
1 JAILBREAK your kindle (Yes this is a must)
2 get PYTHON 3 for kindle (will add links later)
3 get mkk (mobileread kindle kit or something)
4 get KUAL this will be the launcher
5 connect your kindle to your pc and copy the extensions folder in the repo to kindle root folder that you see 
6 run kual and then select the GENERATE pin option and click it 
7 open idrees.hackclub.app
8 enter the pin you got from your kindle
9 upload your file 
10 once it says SAVED go to your kindle and run kual -> check for books
11 the book will appear after some time
12 the next time you do NOT need to regenerate the code
```

```
links : https://www.mobileread.com/forums/showthread.php?t=225030
download kindle jailbreak , python 3 for kindle ,Mobileread Kindlet Kit ,KUAL
```
  
  new acknowledgements :  
  HACKCLUB NEST for providing hosting
  amazon kindlegen

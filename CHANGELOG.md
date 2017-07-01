# Version 1.3
## A huge update to fix and make improvements like :
- [Feature] Adding spoof extension feature so now you can change the file extension and icon to make it full spoof :smile:
- [Improve] Added OSX support ( Thanks to @sm4sh3r )
- [Improve] Now there will be debug file when happen error in compiling with Pyinstaller.
- [BUG fix] Full rewriting the framework to improve the executions methods and fix all the errors
- [BUG fix] Bypassed the error in the Pyinstaller **"FATAL ERROR"** with replacing subprocess Pipes with files :smile:
- [Stealth] Escaping disk forensics by making all the files dropper create and dropper also cleans its content before deletion.
- [Feature] Adds ZIP files support so now you can compress your executable to zip file before uploading
- [Feature] Added Dr0p1t-Server feature (beta) so now you can work from browser [See how to work with Dr0p1t-Server](https://github.com/D4Vinci/Dr0p1t-Framework#work-with-dr0p1t-server)
- [Feature] Added Scamming feature (beta) to Dr0p1t-Server [See how to edit Dr0p1t-Server scam ](https://github.com/D4Vinci/Dr0p1t-Framework#work-with-dr0p1t-server)
- [Stealth] Clear event log after finishing
- [Improve] Added install.sh to make installing on Linux more easy
- [Improve] Persistence modules are now improved and recoded to work much better.
- [Feature] Added new a new-hard-to-detect persistence module ( Adding your file to powershell user profile so your file will be downloaded and ran every time powershell.exe run if it doesn't exist).
- [Feature] Added a new module to bypass UAC and run your malware as admin


# Version 1.2
## A huge update to fix some things like add-cross compile problem and some improvements :
- Pyinstaller compiling in Linux using wine
- Pyinstaller compiling in Windows will not use UPX and that will fix the compiling in windows
- Added the ability to disable and bypass UAC
- Updated the antivirus list in the antivirus killer
- Added SelfDestruct function so that the dropper will kill and delete itself after finishing it work :smile:
- Full framework rewrite and recheck to fix errors, typos and replacing some libraries to make the size of the final file smaller
- Started working in some SE tricks to fool the user and there's a lot of good options in the way ;) **Stay Tuned**

# Version 1.1 ( Stable )
## Now it can be called a stable version and done some things like :
- Added python 2 support ( Now the script can run on python2 or python3 )
- Added option to not compile the script to exe ( if you want to compile dr0p3r by yourself or any other reason )
- Some modifications for sandbox bypass
- Made folder for icons and put some icons in it ( default icons )
- Some improvements and fixes.

# Version 1.0.1 (Beta )
## A small update to fix and improve some things like :
- Considering the size I replaced importing the whole module with importing what I want from the module .
- Improving the task persistence module and bypassing UAC error by creating two tasks with a different names and paths ( one of them runs every hour and the other runs every day ) .
- Improved Run(BAT|PS1|VBS) module to hide the script before running it .
- Improved or fixed the startup persistence module .
- Some improvements and fixes.

# Version 1.0 (Alpha)
### The first release :smile:

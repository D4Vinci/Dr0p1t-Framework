sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get install wine32
sudo winecfg
sudo wine msiexec /i python-2.7.12.msi /L*v log.txt
sudo wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller

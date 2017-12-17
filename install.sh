sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get install wine32
winecfg
wget https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi
wine msiexec /i python-2.7.14.msi /L*v log.txt
wget https://bootstrap.pypa.io/get-pip.py
wine ${HOME}/.wine/drive_c/Python27/python.exe get-pip.py
wine ${HOME}.wine/drive_c/Python27/python.exe -m pip install pyinstaller

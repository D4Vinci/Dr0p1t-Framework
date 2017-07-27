sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get install wine32
sudo winecfg
sudo wget https://www.python.org/ftp/python/2.7.1/python-2.7.1.msi
sudo wine msiexec /i python-2.7.12.msi /L*v log.txt
sudo wget https://bootstrap.pypa.io/get-pip.py
sudo wine /root/.wine/drive_c/Python27/python.exe get-pip.py
sudo wine /root/.wine/drive_c/Python27/python.exe -m pip install pyinstaller

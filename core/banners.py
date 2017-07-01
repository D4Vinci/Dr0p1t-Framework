#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
from core.color import *
from core import color
from os.path import *
import random,os
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
''', open(os.path.join( os.path.dirname(__file__),"logos", "spider_banner.txt" ) ).read(),
open(os.path.join( os.path.dirname(__file__),"logos", "brain_banner.txt" ) ).read(),
open(os.path.join( os.path.dirname(__file__),"logos", "butterfly_banner.txt" ) ).read()
]

info = "\tAuthor  : Karim Shoair ( D4Vinci )\n\tVersion : {}  Codename : {}".format( open( join( dirname(__file__), 'version.txt') ,"r" ).read().strip(), open( join( dirname(__file__), 'codename.txt') ,"r" ).read().strip() )

def random_banner():
    global G, Y, B, R, W , M , C , end
    c1=R
    set_colors()
    c2 = random.choice([G, Y, B, M , C])
    banner = random.choice(banners)
    print_banner( banner ,info ,c1 ,c2 )

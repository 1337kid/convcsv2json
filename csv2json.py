#!/usr/bin/python3
import json,csv,sys,os
from colorama import Fore,Back,Style
def banner():
    print(Fore.BLUE,Style.BRIGHT+'''
   ____ ______     ______     _ ____   ___  _   _ 
  / ___/ ___\ \   / /___ \   | / ___| / _ \| \ | |
 | |   \___  \ \ / /  __) |  | \___ \| | | |  \| |
 | |___ ___) |\ V /  / __/ |_| |___) | |_| | |\  |
  \____|____/  \_/  |_____\___/|____/ \___/|_| \_|
        @1337kid             v1.2.1
        ''')
def help():
    print(Fore.CYAN+'''
    Usage  : csv2json infile outfile [indent]
    Example: csv2json test.csv outfile.json
           : csv2json test.csv outfile.json 2
    ''')
    sys.exit()
def col_prnt(msg,msg_i):
    if msg_i=='info':print(f'{Fore.YELLOW}[+] {Fore.GREEN}{msg}')
    elif msg_i=='err':print(f'{Back.RED+Fore.WHITE}{msg}{Style.RESET_ALL}')
def conv_csv(in_file,out_file,ind):
    col_prnt(f'Opening "{in_file}"','info')
    if os.path.exists(in_file)==0:
        col_prnt(f'"{in_file}" does not exists','err')
        sys.exit()
    with open(in_file) as f:
        data=list(csv.DictReader(f))
    d={}
    col_prnt(f'Generating JSON','info')
    for i in range(len(data)):
        d[i+1]=data[i]
    with open(out_file,'w') as jf:
        if ind!=None:json.dump(d,jf,indent=ind)
        else:json.dump(d,jf)
    col_prnt(f'Saved to "{out_file}"','info')
    Style.RESET_ALL
#=====
try:
    banner()
    if len(sys.argv)<3:help()
    elif len(sys.argv)==3:conv_csv(sys.argv[1],sys.argv[2],None)
    elif len(sys.argv)==4:conv_csv(sys.argv[1],sys.argv[2],int(sys.argv[3]))
except KeyboardInterrupt:col_prnt('KeyboardInterrupt','err')
except ValueError:col_prnt('"intent" argument must be an integer','err')
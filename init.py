import sys
import os

#this will take the ip and the box
ip = sys.argv[-2]
box = sys.argv[-1]

#create a directory and a simple nmap scan
def nmap():
        print('\x1b[2;3;44m'+ f"\nthe box is '{box}' and the IP Address is {ip}".title() + '\x1b[0m')
        os.system('mkdir ' + box)
        os.system(f'nmap -Pn -T4 -oN {box}/quick_nmap.txt ' + ip)
        print('\x1b[2;3;44m'+ f"\nquick_scan is done!" + '\x1b[0m')
        os.system(f'nmap -Pn -sC -sV -v -p- -oN {box}/nmap.txt ' + ip)
        os.system('mv ' + ip + ' ' + box)
        print('\x1b[2;3;44m'+ f"\na directory called '{box}' has been opened and an nmap quick scan result has been saved titled as {ip}".title() + '\x1b[0m')

nmap()

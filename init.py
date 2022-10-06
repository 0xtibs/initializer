import sys
import os

ip = sys.argv[-2]
box = sys.argv[-1]

print('\x1b[2;3;44m'+ f"\nthe box is '{box}' and the IP Address is {ip}".title() + '\x1b[0m')

os.system('mkdir ' + box)

os.system(f'nmap -Pn -sC -sV -v -oN {box}/nmap.txt ' + ip)
#os.system('mv ' + ip + ' ' + box)

print('\x1b[2;3;44m'+ f"\na directory called '{box}' has been opened and an nmap quick scan result has been saved titled as {ip}".title() + '\x1b[0m')

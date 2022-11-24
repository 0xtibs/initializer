import sys
import os


#this will take the ip and the box
ip = sys.argv[-2]
box = sys.argv[-1]

#create a directory and a simple nmap scan
def nmap():
	print('\x1b[2;3;44m'+ f"\nthe box is '{box}' and the IP Address is {ip}".title() + '\x1b[0m')

	os.system('mkdir ' + box)

	os.system(f'nmap -Pn -sC -sV -v -p- -oN {box}/nmap.txt ' + ip)
	os.system('mv ' + ip + ' ' + box)

	print('\x1b[2;3;44m'+ f"\na directory called '{box}' has been opened and an nmap quick scan result has been saved titled as {ip}".title() + '\x1b[0m')

def port80():
	os.chdir(f'{box}')
	with open("nmap.txt", 'r') as scan:
		lines = scan.read()
		print(lines)

# check if it has port 80 available
		web = "80/tcp"
		if web in lines:
			print("\x1b[2;3;44m Has a web application running \x1b[0m")
# start directory busting using wfuzz
			os.system(f'wfuzz -w /usr/share/KaliLists/dirbuster/directory-list-2.3-medium.txt http://{ip}/FUZZ')



		else:
			print("No port 80")

	

nmap()
port80()

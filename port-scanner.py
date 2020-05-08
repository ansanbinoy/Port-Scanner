from os import system as sys
try :
	from termcolor import colored
	from time import sleep
	import socket
except ModuleNotFoundError :
	sys("python install.py")
sys("clear")
def banner():
	sys("cat banner.txt")
try :
	print("\033[1;31;40m")
	banner()
	print ("\t \t\t<[----- coded By SHADOW ANON -----]>")
	print ("")
	g = (colored("[~]",'green'))
	y = ("\033[1;35m[+]")
	c =(colored("[~]",'cyan'))
	b = (colored("[~]",'blue'))
	gm = (colored("[-]",'green'))
	tip = input(gm + " \033[1;32mTarget host : \033[1;37m")
	print ("")
	tport = input(gm + " \033[1;32mPort range [Eg:(80-90) :\033[1;37m ")
	lport = int(tport.split('-')[0])
	rport = int(tport.split('-')[1])
	hport = rport+1
	print (colored("<===================================>",'white'))
	def scan( ip, port1, port2):
		for port in range(port1, port2):
		 	socket.setdefaulttimeout(1)
		 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		 	socket.setdefaulttimeout(1)
		 	status = s.connect_ex((ip, port))
		 	sleep(0.5)
		 	print("")
		 	print (c + " \033[1;32mScanning port {}".format(port))
		 	if status==0:
		 		sleep(1)
		 		print(colored("  \t" + y +" \033[1;32mPort {} Open".format(port),'green'))
		 	else :
		 		sleep(1)
		 		print ("  \t"+ b + " \033[1;31mPort {} Close".format(port))
		 		s.close()
	scan(tip, lport, hport)

except Exception as e:
	print (e)
except KeyboardInterrupt:
	print(colored("[!] Exiting....",'red'))
	sleep(1)
	exit()
except socket.error as s:
	print(s)
except socket.gaierror as gs:
	print(gs)
except ConnectionRefusedError as cn:
	print (cn)

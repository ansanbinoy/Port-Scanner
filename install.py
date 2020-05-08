from os import system as sys
try :
  sys("pip install termcolor")
  sys("pip install socket")
except KeyboardInterrupt :
  print ("[!] Installing Failed")
except IOError as err :
  print ("err")

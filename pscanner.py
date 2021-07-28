#!/bin/python

import sys	
import socket 
from datetime import datetime

# Defining Target
if len(sys.argv) == 2:
	#hostname to IPV4
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments")
	print("usage: python3 pscanner.py $ip")
	
# Banner 
print("_" * 50)
print("Scanning: "+target)
print("Time started: "+str(datetime.now()))
print("_" * 50)

try:
	for port in range(1,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		# Returns an error (indicator)
		result = s.connect_ex((target,port))
		if result == 0: 
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("Keyboard Interrupt, Exiting Program")
	sys.exit()
	
except socket.gaierror: 
	print("Hostname Could not be resolved")
	sys.exit()

except socket.error:
	print("Connection to the server failed")
	sys.exit()
	
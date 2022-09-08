# This code is bade on https://www.geeksforgeeks.org/port-scanner-using-python/
# Few modifications were made by enricofd

import sys
import socket
from datetime import datetime

# Add Initial Banner
print("-" * 50)
print("Welcome to port scanner")
print("-" * 50)

# Defining a target
try:
    target = socket.gethostbyname(input("Please insert an ip to be scanned: "))
except:
    raise Exception("Could not convert input to host.")

print("-" * 50)

# Defining range of ports to be scanned
try:
    initial_port = int(input("Please insert the initial port to be scanned: "))
except:
    raise Exception("Could not convert input to integer")

try:
    final_port = int(input("Please insert the final port to be scanned: "))
except:
    raise Exception("Could not convert input to integer")

print("-" * 50)

# Starting scan
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
# will scan ports
    for port in range(initial_port, final_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

    #  returns an error indicator
        result = s.connect_ex((target,port))

        if result == 0:
            service = socket.getservbyport(port, "tcp")
            print(f"Port: {port} is open - Service: {service} is running;")
        s.close()
		
except KeyboardInterrupt:
		print("\n Exiting Program !!!!")
		sys.exit()

except socket.gaierror:
		print("\n Hostname Could Not Be Resolved !!!!")
		sys.exit()

except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()


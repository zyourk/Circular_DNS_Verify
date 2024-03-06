# Taking care of imports used in the program
import dns.resolver
import dns.reversename
import sys
import os
import socket
sys.path.append('usr/lib/python3/dist-packages')

# Define the subnet you wish to search through here
SUBNET = "" 

# Loops through the full range, properly formatting the IPs and hostnames
for i in range(1, 256):
    IP = SUBNET + "." + str(i)
    try:
        temphost = str(socket.gethostbyaddr(IP))
        host = ""
        currentchar = ''
        i = 2
        while currentchar != "'":
            host += currentchar
            currentchar = temphost[i]
            i += 1
    except:
        print("%s not resolved to hostname" %(IP))
    else:
        # Checks to ensure the host exists (if it has been formatted it will) and then 
        # Performs a reverse lookup to ensure they IPs match
        if host:
            result = socket.gethostbyname(host)
            if IP == result:
                print("OK: %s -> %s -> %s" %(IP, host, result))
            elif result:
                print("FAIL: %s -> %s -> %s" %(IP, host, result))
            else:
                print("FAIL: %s -> %s -> unassigned" %(IP, host))
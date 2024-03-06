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
    # Checks to ensure the host is pingable before carrying on through the process
    # Note: Using the c switch in this command does require permissions. Ensure you have them before running.
    response = os.system("ping -c 1 " + IP)
    if response == 0:
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

    # The else case has been considered, but is not needed as
    # We don't want to do anything with the IP if it is not pingable
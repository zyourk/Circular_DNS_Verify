# Taking care of imports used in the program
import dns.resolver
import dns.reversename
import sys
import os
import socket
sys.path.append('usr/lib/python3/dist-packages')

# Define the subnet you wish to search through here
SUBNET = "X.X.X" 

# Setting the sentinel value to one that will keep the while loop going
ping_prompt = 2

# While loop prompting user for response until a valid response is given
while ping_prompt != 0 and ping_prompt != 1:
    ping_prompt = int(input("Would you like to check if each IP is pingable before resolving? 0 - yes, 1 - no\n"))
    if ping_prompt != 1 and ping_prompt != 0:
        print("Invalid response, please input again")
    

# Loops through the full range, properly formatting the IPs and hostnames
for i in range(1, 256):
    IP = SUBNET + "." + str(i)
    # Checks to ensure the host is pingable before carrying on through the process (given the user chose to)
    # Note: Using the c switch in this command does require permissions. Ensure you have them before running.
    if ping_prompt == 0:
        response = os.system("ping -c 1 " + IP)
    # Checks first if the user chose no, if not then checks if the box was pingable
    if (ping_prompt == 1 or response == 0):
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

    # The else case has been considered, but is not needed
from socket import *
from time import time, ctime
import sys
import os

# Checking to see if we have three arguments
if len(sys.argv) != 3:
    print("Wrong number of arguments.")
    print(f"Enter Command on CLI: python3 {os.path.basename(__file__)} {gethostbyname(gethostname())} 12000")
    sys.exit()

# Preparing the socket
serverHost, serverPort = sys.argv[1:]
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(10):
    startTime = time() # Retrieve the current time
    message = "Ping " + str(i+1) + " " + ctime(startTime)[11:19]

    try:
        # Sending the message and waiting for the answer
        clientSocket.sendto(message.encode(), (serverHost, int(serverPort)))
        encodedModified, serverAddress = clientSocket.recvfrom(1024)

        # Checking the current time and if the server answered
        endTime = time()
        modifiedMessage = encodedModified.decode()
        print(modifiedMessage)
        print("RTT: %.3f ms\n" % ((endTime - startTime)*1000))
    except TimeoutError:
        print("PING #%i Request timed out\n" % (i+1))

clientSocket.close()

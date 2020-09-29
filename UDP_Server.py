# UDPPingerServer.py
# CODE TAKEN FROM THE COMPANION GUIDE FOR THIS ASSIGNMENT.
# We will need the following module to generate randomized lost packets
import random
from socket import *


# HOST_NAME = gethostbyname(gethostname())
HOST_NAME = '127.0.0.1'
HOST_PORT = 12000

print(f"Host Name: {HOST_NAME}")
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind((HOST_NAME, HOST_PORT))

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    print(rand)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()
    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)
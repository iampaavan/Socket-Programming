import glob
import os
import sys
from socket import *

current_directory = os.getcwd()


def prepare_socket():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    return clientSocket


def get_network_parameters():
    serverHost, serverPort, filename = sys.argv[1:]
    return serverHost, serverPort, filename


try:
    # Preparing the socket
    network_parameters = get_network_parameters()
    prepare_socket()

except ValueError:
    # Checking to see if we do have four arguments
    if len(sys.argv) != 4:
        print("Wrong number of arguments.")
        text_file = ''
        for text_file_name in glob.glob(os.path.join(current_directory, 'sample.txt')):
            text_file = text_file_name
        print(f"Use: python3 {os.path.basename(__file__)} {gethostbyname(gethostname())} {text_file}")
        sys.exit()

try:
    clientSocket = prepare_socket()
    clientSocket.connect((get_network_parameters()[0], int(get_network_parameters()[1])))

# If the HTTP Server is not available
except ConnectionError:
    print("Sorry, the server is currently offline or busy.")
    clientSocket = prepare_socket()
    clientSocket.close()
    sys.exit()

print("Connection Established.")

# Sending the HTTP request
httpRequest = "GET /" + get_network_parameters()[2] + " HTTP/1.1\r\n\r\n"
clientSocket.send(httpRequest.encode())
print("Request message sent.")

# Receiving the response
print("Server HTTP Response:\r\n")


data = ""
while True:
    clientSocket.settimeout(5)
    newData = clientSocket.recv(1024).decode()
    data += newData

    if len(newData) == 0:
        break

print(data)

# Closing socket and ending the program
print("Closing socket . . .")
clientSocket.close()

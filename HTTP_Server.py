# Import socket module
# Import sys to terminate the program
from socket import *
import sys

# Get the HostName or HostServer
print("\n" + gethostbyname(gethostname()))

# Preparing the server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((gethostname(), 5432))

# Waiting for a request
serverSocket.listen(1)

print("HTTP Server Up and Running !!!!")

while True:
    # Accepting request
    connectionSocket, addr = serverSocket.accept()
    print("Request accepted from (address, port) tuple: %s" % (addr,))

    try:
        # Receive message and check file name
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]
        try:
            if not filename:
                print('File Not Found')
        except FileNotFoundError:
            sys.exit()

        f = open(filename[1:], 'r')
        outputdata = f.read()

        result = outputdata.capitalize()
        # Returns header line informing that the file was found
        headerLine = "HTTP/1.1 200 OK\r\n"
        connectionSocket.send(headerLine.encode())
        connectionSocket.send("\r\n".encode())

        # Sends the file
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        print('*************************************************************************************')
        print('\n')
        print('******************************RESULT BELOW*******************************************')
        print('\n')
        print(f'Server Message Before Reverse: {result}')
        print('\n')
        print("*****************************After Reverse*******************************************")
        print('\n')
        print(f"Server Message: {result[::-1]}")
        print('\n')

        # Terminates the connection
        connectionSocket.close()

    except IOError:
        print("Warning: file not found.")

        # Returns the error header to the browser
        errHeader = "HTTP/1.1 404 Not Found\r\n"
        connectionSocket.send(errHeader.encode())
        connectionSocket.send("\r\n".encode())

        # Opens and sends the error page to the browser
        ferr = open("not_found.txt", 'r')
        outputerr = ferr.read()

        for i in range(0, len(outputerr)):
            connectionSocket.send(outputerr[i].encode())
        connectionSocket.send("\r\n".encode())

        # Terminates the connection
        print("Error message sent.")
        connectionSocket.close()

    # Closes the application
    serverSocket.close()
    sys.exit()

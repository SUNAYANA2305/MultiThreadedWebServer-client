# Name: Sunayana Ambakanti
# SAU ID: 999901013

# Import socket module
# Import sys to terminate the program
from socket import *
import sys
import datetime

# Preparing the socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12345

if len(sys.argv) == 2:
    ServerPort = int(sys.argv[1])
Host = gethostname()
# Binding the port to the socket
serverSocket.bind(('',serverPort)) 
# Waiting for a request(time)
serverSocket.listen(5) 
print("Ready to serve . . .")
filename=""

while True:
    # Establishing the connection
    connectionSocket, addr = serverSocket.accept() # Accepting request
    # Host Name of the Client, socket family, socket type, protocol, timeout and get peer name
    print("Request accepted from (address, port) tuple: %s" % (addr,))
    print("TimeStamp", datetime.datetime.now(), "Request from", (gethostbyaddr(connectionSocket.getpeername()[0]))[0],
          (gethostbyaddr(connectionSocket.getpeername()[0]))[2])
    print("Client Host Name:",(gethostbyaddr(connectionSocket.getpeername()[0]))[0])
    print("Client Socket Family:", connectionSocket.family)
    print("Client Socket Type:", connectionSocket.type)
    print("Client Protocol:", connectionSocket.proto)
    print("Client Timeout:", connectionSocket.gettimeout())
    print("Client Socket- get Peer Name:", connectionSocket.getpeername())

    try:
        # Recieve message and check file name
        message = connectionSocket.recv(2048).decode()
        if message != '':
            print("Request details:", message)
        filename = message.split()[1]
        f = open(filename[1:], 'r')
        outputdata = f.read()
        print(outputdata)
        print("File found.")
        # Returns header line informing that the file was found
        headerLine = "HTTP/1.1 200 OK\r\n"
        connectionSocket.send(headerLine.encode())
        connectionSocket.send("\r\n".encode())

        # Sends the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        print("File sent to client...")
        #closing the socket
        connectionSocket.close()

    #File not found
    except IOError: 
        print("message",message)
        if filename!="/favicon.ico":
            print(IOError)
            print("Response:404 File Not Found sent to client")
            print("\n")
        else:
            print("Additional request sent by Browser")
            print("\n")
        connectionSocket.send("\n404 File Not Found\n")
        # closing sockets
        connectionSocket.close() 
# closing server socket
ServerSocket.close()
sys.exit()
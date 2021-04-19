# Name: Sunayana Ambakanti
# SAU ID: 999901013

# import the socket module
# import sys forcommandline functions
# import time to calculate RTT
from socket import * 
import time
import sys  
import datetime 

#preparing the socket
# IPV4 address, TCP stream
ClientSocket = socket(AF_INET, SOCK_STREAM) 

# if port number is provided
if (len(sys.argv)==4): 
    IPaddress=str(sys.argv[1])
    Portno=int(sys.argv[2])
    filename=str(sys.argv[3])
# if port number is not provided default port is 8080
if (len(sys.argv)==3):
    IPaddress=str(sys.argv[1])
    Portno=8080
    filename=str(sys.argv[2])

ServerPort=Portno
Host = IPaddress
endtime=0 
# connect to the Server ip with portno
ClientSocket.connect((Host,ServerPort)) 
# Host Name of the server, socket family, socket type, protocol, timeout and get peer name
print ("TimeStamp: ",datetime.datetime.now(),"Request to", (gethostbyaddr(ClientSocket.getpeername()[0]))[0],(gethostbyaddr(ClientSocket.getpeername()[0]))[2])
print ("Server Host Name:",(gethostbyaddr(ClientSocket.getpeername()[0]))[0])
print ("Server Socket Family:",ClientSocket.family)
print ("Server Socket Type:",ClientSocket.type)
print ("Server Protocol:", ClientSocket.proto)
print ("Server Timeout:",ClientSocket.gettimeout())
print ("Server Socket get Peer Name:", ClientSocket.getpeername())

#initialize the output as null
output="" 
url_params=(IPaddress+str(ServerPort),('/'+filename))
url=" ".join(url_params)
# RTT start time
starttime=time.time() 
temp = url+"\n"

ClientSocket.send(temp.encode())
print("Request sent to Server:", url)
while True:
    # receive the response from the server
    response=ClientSocket.recv(2048)

    # capture time for the 1st response
    if (endtime==0): 
        endtime=time.time()# end time for RTT
    if response=="":
        break
    sys.stdout.write(response) 
    
#RTT calculation
RTT=endtime-starttime 
print ("RTT is", RTT ,"Seconds")

 # closing the socket
ClientSocket.close() 
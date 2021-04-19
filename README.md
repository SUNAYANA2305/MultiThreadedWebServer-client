# MultiThreadedWebServer-client
Project Description:
Developing a multi-threaded Web server which interacts with any standard Web Clients. The Web server and Web client communicate using a text-based protocol called HTTP (Hypertext Transfer Protocol).

Project Environment:
Python 2.7.18 IDE
Google chrome
Windows Command prompt

Execution steps:
To run Server:
1. Open command prompt change the directory path to the one which contains the server.py python file.  (C:\Users\sunay\PycharmProjects\CN_Project)
2. Running the server program using command line
Syntax: Server_code_name < port_number >  
Ex: "python server.py 12345" 
3. Web server implementation on local machine using a Web browser.
http://127.0.0.1:12345/HelloWorld.html

To Run Client:
4. Open another Command Prompt, Change the directory path to the one which contains the client.py python file. (C:\Users\sunay\PycharmProjects\CN_Project) 
5. To Run the Client , Syntax is http ∶ //localhost ∶ 8080/index.html 
Ex: “python client.py 127.0.0.1 12345 HelloWorld.html”

References:
1.	Skeleton code provided for python.
2.	https://docs.python.org/2/howto/sockets.html
3.	http://bytes.com/topic/python/answers/932033-help-message-splitting-code
4.	https://docs.python.org/2/library/socket.html
5.	https://www.geeksforgeeks.org/socket-programming-python

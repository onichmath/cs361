# CS361 Project - Hash Service
This program maintains Blake2b hashes for files on your computer, so that you may check if the files have been tampered with.

## Communication Contract
Communication with the trails microservice is done using the ZeroMQ module. The ZeroMQ module makes use of sockets and the TCP protocol to send and receive data.

#### Requesting Data
Data is requested from the server in the form of an SQL query, translated into a string and sent over the TCP protocol. A REQSocket class socket variable is made that instantialized a connection, with default connection being made to localhost port 5555.
Request data using this object with these steps:
1. Create REQSocket object socket variable named SOCKET
2. Pass in request to REQSocket object using: SOCKET.send_string(request)
3. Receive server response with SOCKET.recv_string()

#### Receiving Data
Data is received over the TCP protocol, using a REPSocket class object that instantialized a REPSocket to port 5555 by default. 
Data is recieved following these steps:
1. Create a REPSocket object socket variable named SOCKET
2. Receive query by using SOCKET.recv_string()
3. Parse and execute query
4. Return results with SOCKET.send_string()

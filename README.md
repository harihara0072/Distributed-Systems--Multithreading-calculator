# Distributed-Systems--Multithreading-calculator

## Language used :
Python 3.7

### Libraries used:
Tkinter
Threading
Socket

### Server.py
1. Created a socket in the server by giving the host name and port number
2. Server will be continuously listening for the clients
3. Once a client is connected then the server sends a HTTP GET request to the client asking for the username
4. Once we get the response from the client then it will create a new thread.
5. Once the Pull button is clicked on the server then it will ask all the clients connected to send the set of operations that it has executed from the previous pull
6. Then the server will evaluate all the set of operations together and update its local value
7. Server will update all the clients with the new local value.
8. Server will be keep doing this until it is closed.

### Client.py:
1. The client will connect to the server socket by using server hostname and port number.
2. Then the client will receive the HTTP GET request for the username and client will respond to it.
3. The client will accept the operations from the user and will execute them on its local value.
4. The client will also log the set of operations from the previous pull.
5. Once the client receives the pull request then it will send all the set of its local operations to the server
6. The client will wait for the server to respond with the new local value and once it gets it then it will update its local value with that and performs the next operations on that.
7. The client will keep doing this until it is closed by the user.

### Code running structure:
python server.py
python client.py(3 times for 3 clients)

from time import sleep

# Sockets are a way of sending data over a network.
# There are two main types of sockets, TCP and UDP.
# Which to use depends on the application you are communicating with.

# Import the socket library first.
import socket

# To make a connection to a TCP server:

# Create a socket. AF_INET means you're connecting to an IPv4 IP
# Address.
# SOCK_STREAM means you are connecting over TCP and not UDP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tell the socket what IP Address and Port number to connect to.
clientsocket.connect(('127.0.0.1', 9987))
# Send some data over the socket.
clientsocket.send('hello')
# Receive some data back. The 1024 is the max number of bytes of data
# to accept.
data = clientsocket.recv(1024)
print(data)

# You should see "You said: hello" printed out. That's because our
# server is setup to respond to whatever you send it by adding
# You said: to the front of it and sending it back.

# To make a TCP Server:

# Create a socket.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to listen to a port.
serversocket.bind(("127.0.0.1", 9985))
# Tell the socket to start listening.
# The 10 is the maximum number of connections.
serversocket.listen(10)

# Setup an infinite loop so the socket will keep listening for
# incoming connections.
while True:
    # If it gets a new connection, accept it and save the connection
    # and address.
    connection, address = serversocket.accept()
    # Read 1024 bytes of data from the connection.
    data = connection.recv(1024)
    # Check the length of data. If the length is more than 0 then
    # that means something was sent, so print it out.
    if len(data) > 0:
        print("Received: " + data)

    # Close the connection.
    connection.close()
    # We don't need to keep listening any more so break out of the
    # infinite loop
    break

# Close the socket.
serversocket.close()

sleep(0.05)

# CHALLENGE 1: Write a TCP Client that will connect to 127.0.0.1 on
#              port 9990.
#              Your client must send "Knock, knock" to the server.
#              Then get the response, and print it out.


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 9990))
clientsocket.send('Knock, knock')
data = clientsocket.recv(1024)
print(data)
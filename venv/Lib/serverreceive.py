# Write a server that listens on ('localhost', 10000).
# The flag will be sent to that address
# record signal to /tmp/aliensignallog.txt

import socket

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\n")

# Open a socket, bind and listen to it
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 10000))
serversocket.listen(10)

# Accept connections
conn, address = serversocket.accept()

# Open a text file to write received signals to
signallog = open("/tmp/aliensignallog.txt", "w")

# Recieve data and keep writing until there is no data left to receive
while True:
  data = conn.recv(2048)
  if not data:
    break
  signallog.write(data)

# Close the socket
serversocket.close()
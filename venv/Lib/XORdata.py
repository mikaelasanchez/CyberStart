#
# Setup server listening on ('localhost', 10000)
# receive data then send back XORed with the key
# attackthehumans
#
# If you get an address already in use error then try again in a few
# moments.
#

import socket
from itertools import cycle

def do_xor(key, str):
	str = str.replace(' ', '')
	key = ''.join(key.split()[::-1])
	return ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(str, cycle(key))])

def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\n")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 10000))
serversocket.listen(10)
conn, address = serversocket.accept()

while True:
  data = conn.recv(2048)
  sendback = do_xor('attackthehumans', data)
  conn.send(sendback)
  conn.close()
  break
import socket
from Client0 import Client
# SERVER IP, PORT
PORT = 8070
IP = "127.0.0.1"

c = Client(IP, PORT)
for n in range(1,6):
    c.debug_talk(str(n))

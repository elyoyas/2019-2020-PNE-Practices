import socket
from Client0 import Client
# SERVER IP, PORT
PORT = 8080
IP = "127.0.0.1"

c = Client(IP, PORT)
print(c.talk('HI'))

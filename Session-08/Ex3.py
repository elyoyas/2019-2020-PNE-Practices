import socket

# SERVER IP, PORT
PORT = 2345
IP = "127.0.0.1"

while True:
  # -- Ask the user for the message
    content= input("select a message: ")
  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # -- Establish the connection to the Server
    s.connect((IP, PORT))

  # -- Send the user message
    s.send(str.encode(content))
  # -- Close the socket
    s.close()
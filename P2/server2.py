import socket
# Configure the Server's IP and PORT
PORT = 2346
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
connect = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        connect += 1

        print("CONNECTION: {}. From the IP: {}".format(connect, address))

        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        message = "Hello from the teacher's server"
        send_bytes = str.encode(message)
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}.".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

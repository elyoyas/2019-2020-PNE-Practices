import socket
import termcolor

class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("testing Client0.py \n OK!!")

    def __str__(self):
        print(f"Connection to SERVER at {self.ip}, PORT: {self.port}")

    def talk(self,msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response

    def debug_talk(self, msg):
        message = str(msg)
        response = self.talk(msg)
        print("To server:")
        termcolor.cprint(f"{message}", "blue")
        print('From server:')
        termcolor.cprint(f' {response}',"green")
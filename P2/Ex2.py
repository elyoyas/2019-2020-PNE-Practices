from Client0 import Client
PRACTICE = 2
EXERCISE = 2
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "192.168.56.1"
PORT = 8080
c = Client(IP, PORT)

c.__str__()

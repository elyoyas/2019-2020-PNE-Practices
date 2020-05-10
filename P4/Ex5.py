import socket
import termcolor
from pathlib import Path


# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")
    lines = req.split('\n')
    req_line = lines[0]
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")
    req_meths= req_line.split(" ")
    method = req_meths[0]
    path = req_meths[1]
    response_body= ""

    if method == "GET":
        if path == "/info/A":
            response_body = Path("A.html").read_text()
        elif path == "/info/C":
            response_body = Path("C.html").read_text()
        elif path == "/info/G":
            response_body = Path("G.html").read_text()
        elif path == "/info/T":
            response_body = Path("T.html").read_text()
        else:
            response_body = Path("ERROR.html").read_text()

    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(response_body)}\n"
    response_msg = status_line + header + "\r\n" + response_body
    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))

ls.listen()

print("Server on")

# --- MAIN LOOP
while True:
    print("Expecting client connections")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped by user")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()
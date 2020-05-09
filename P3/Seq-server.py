import socket
import termcolor
from Seq1 import *
# Configure the Server's IP and PORT
PORT = 8090
IP = "127.0.0.1"
folder = "../Session-04/"

listensock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listensock.bind((IP, PORT))
listensock.listen()

genelist=["ACACACACACACACACACACACACACACACACACACACACA","ATATATATATATATTATATATATATATATATATATATA","CGTACGATCGAGAGAG","GGGGGGGGGGGGGGGGGGGGGGGGGGG","AAACCCTTTGGGG"]
Open= True

def listen():
    print(f"Waiting for connections (IP,PORT:{IP,PORT})")
    (cs, client_ip_port)=listensock.accept()
    print("A client has connected to the server!")
    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    return [msg,cs]

#Server runs on a loop until the CLOSE command is sent
while Open:
    m = listen()
    if "PING" in m:
        termcolor.cprint("PING command!", 'green')
        print("OK!")
        r = "OK!\n"
        m[1].send(r.encode())
    elif "GET" in m[0]:
        termcolor.cprint("GET requested", "green")
        num=int(m[0][-1])
        r=genelist[num]
        print(r)
        m[1].send(r.encode())
    elif "INFO " in m[0]:
        termcolor.cprint("INFO requested", "green")
        seq = Seq(m[0][5:])
        r=(f"SECUENCE:{seq.__str__()} Length:{seq.len()}\n")
        for element in seq.seq_count():
            percent = seq.seq_count()[element]/seq.len()*100
            r+=(f"\n{element}: {seq.seq_count()[element]} ({percent}%)")
        print(r)
        m[1].send(r.encode())
    elif "COMP" in m[0]:
        termcolor.cprint("COMP requested", "green")
        seq = Seq(m[0][5:])
        r= seq.seq_complement()
        print(r)
        m[1].send(r.encode())
    elif "REV" in m[0]:
        termcolor.cprint("REV requested", "green")
        seq = Seq(m[0][4:])
        r= seq.seq_reverse()
        print(r)
        m[1].send(r.encode())
    elif "GENE" in m[0]:
        termcolor.cprint("GENE requested", "green")
        seq=Seq("")
        file=folder+m[0][5:]+".txt"
        r=str(seq.seq_read_fasta(file))
        print(r)
        m[1].send(r.encode())
    elif "CLOSE" in m:
        termcolor.cprint("CLOSE requested", "green")
        r="server closed"
        m[1].send(r.encode())
        Open = False

#when close is sent it exits the loop and closes the socket
print("server closing")
listensock.close()

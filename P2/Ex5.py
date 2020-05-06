from Client0 import Client
from Seq1 import Seq
from Seq1 import *

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 2345
c = Client(IP, PORT)
FOLDER = "../Session-04/"
file= "U5.txt"
s0 = Seq("").seq_read_fasta(FOLDER+file)

m1="Sending u5 Gene to the server..."
m2=s0.__str__()

c.debug_talk(m1)
c.debug_talk(m2)
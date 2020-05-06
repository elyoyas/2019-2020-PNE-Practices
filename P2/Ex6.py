from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 2345
c = Client(IP, PORT)
FOLDER = "../Session-04/"
txt = ".txt"
gene = "FRAT1"
file_name = FOLDER + gene + txt

s0 = Seq('')
s0 = str(s0.seq_read_fasta(file_name))

size = 10
num_frag = 5
print(f"Gene {gene}: {s0}")
fragments = []
for e in range(num_frag):
    print(f"fragment {e+1}: {s0[size*e:size*(e+1)]}")
    fragments.append(s0[size*e:size*(e+1)])
for number in range(0,5):
    print(c.talk(fragments[number]))

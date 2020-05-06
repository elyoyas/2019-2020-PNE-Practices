from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT1 = 2345
PORT2 = 2346
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

FOLDER = "../Session-04/"
txt = ".txt"
gene = "FRAT1"
file_name = FOLDER + gene + txt

s0 = Seq('')
s0 = str(s0.seq_read_fasta(file_name))

size = 10
num_frag = 10
print(f"Gene {gene}: {s0}")
fragments = []

for e in range(num_frag):
    print(f"fragment {e+1}: {s0[size*e:size*(e+1)]}")
    fragments.append(s0[size*e:size*(e+1)])

for number in range(0,10):
    if (number % 2) == 0:
        print(c1.talk("fragment {}: {}".format(number,fragments[number])))

    elif (number % 2) != 0:
        print(c2.talk("fragment {}: {}".format(number,fragments[number])))

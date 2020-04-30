print('-----| Practice 1, Exercise 10 |------')
from Seq1 import *
FOLDER ="../Session-04/"
file_list = ["U5", "ADA", "FXN", "RNU6_269P","Frat1"]
s0= Seq('')

for file in file_list:
    printed=False
    s0=s0.seq_read_fasta(FOLDER+file+".txt")
    every_count = []
    dictbases = s0.seq_count()
    for key in dictbases:
        every_count.append(dictbases[key])
    ordered_bases = sorted(every_count)
    for element in dictbases:
        if printed==False:
            if dictbases[element] == ordered_bases[-1]:
                print(file,"most frequent base:", element)
                printed=True


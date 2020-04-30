from Seq1 import *
print('-----| Practice 1, Exercise 9 |------')
FOLDER = "../Session-04/"
file= "U5.txt"
s0 = Seq("").seq_read_fasta(FOLDER+file)

print(f"Sequence : (Length: {s0.len()}) {s0}\nBases: {s0.seq_count()}"
      f"\nReverse: {s0.seq_reverse()}\nComplement: {s0.seq_complement()}")

from Seq1 import *
print('-----| Practice 1, Exercise 7 |------')
s1 = Seq('')
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print_seqs(s1,1)
print(f"Bases: {s1.seq_count()}\nReverse: {s1.seq_reverse()}")

print_seqs(s2,2)
print(f"Bases: {s2.seq_count()}\nReverse: {s2.seq_reverse()}")

print_seqs(s3,3)
print(f"Bases: {s3.seq_count()}\nReverse: {s3.seq_reverse()}")

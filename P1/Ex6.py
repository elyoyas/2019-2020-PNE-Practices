from Seq1 import *
print('-----| Practice 1, Exercise 6 |------')
s1 = Seq('')
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print_seqs(s1,1)
print(s1.seq_count())
print_seqs(s2,2)
print(s2.seq_count())
print_seqs(s3,3)
print(s3.seq_count())

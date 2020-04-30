from Seq1 import *
print('-----| Practice 1, Exercise 5 |------')
s1 = Seq('')
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
base_list= ["A",'C','T','G']

print_seqs(s1,1)
for base in base_list:
    print(f'{base}: {s1.count_base(base)}', end=' ')
print('\n')
print_seqs(s2,2)
for base in base_list:
    print(f'{base}: {s2.count_base(base)}', end=' ')
print('\n')
print_seqs(s3,3)
for base in base_list:
    print(f'{base}: {s3.count_base(base)}', end=' ')

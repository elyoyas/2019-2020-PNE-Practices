from seq0 import *

FOLDER = "../Session-04/"
base_list = ["A", "C", "T", "G"]
file_list = ["U5", "ADA", "Frat1", "FXN", "RNU6_269P"]
print("-----| Exercise 4 |------")
for file in file_list:
    print("\nGene ", file, ":", sep="")
    for base in base_list:
        print(base, ":", seq_count_base(FOLDER + file + ".txt", base))

from seq0 import *
FOLDER = "../Session-04/"
file_list = ["U5", "ADA", "Frat1", "FXN", "RNU6_269P"]
print('-----| Exercise 5 |------')
for file in file_list:
    print(seq_count(FOLDER+file+'.txt'))
from seq0 import *
FOLDER ="../Session-04/"
file_list = ["U5", "ADA", "Frat1", "FXN", "RNU6_269P"]
print('-----| Exercise 8 |------')

for file in file_list:
    every_count = []
    dictbases = seq_count(FOLDER+file+'.txt')
    for key in dictbases:
        every_count.append(dictbases[key])
    ordered_bases = sorted(every_count)
    for element in dictbases:
        if dictbases[element] == ordered_bases[-1]:
            print(file,"most frequent base:", element)

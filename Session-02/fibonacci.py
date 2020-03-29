num_1 = 0
num_2 = 0
counter = 0
while counter <= 11:
    num_to_print = num_1 + num_2
    print(num_to_print, end=' ')
    counter += 1
    num_1 = num_2
    num_2 = num_to_print
    if num_2 == 0:
        num_1 += 1
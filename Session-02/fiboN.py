def fibon(n):
    num_1 = 0
    num_2 = 0
    counter = 0
    while counter <= n:
        num_to_print = num_1 + num_2
        counter += 1
        num_1 = num_2
        num_2 = num_to_print
        if num_2 == 0:
            num_1 += 1
    return num_to_print

print("5th fibonacci term:",fibon(5),"\n10th fibonacci term:",fibon(10),"\n15th fibonacci term:",fibon(15))
def fibosum(n):
    num_1 = 0
    num_2 = 0
    counter = 0
    suma = 0
    while counter <= n:
        num_to_print = num_1 + num_2
        counter += 1
        num_1 = num_2
        num_2 = num_to_print
        if num_2 == 0:
            num_1 += 1
        suma += num_to_print
    return suma
print("Sum of the first 5 fibonacci terms:",fibosum(5),"\nSum of the first 10 fibonacci terms:",fibosum(10) )
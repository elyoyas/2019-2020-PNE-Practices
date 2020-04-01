File = open("dna", "r")
text = ""
for line in File:
    content= line.strip("\n")
    text += content
As = 0
Gs = 0
Cs = 0
Ts = 0
valid = True
for item in text:
    if item == "A":
        As += 1
    elif item == "C":
        Cs += 1
    elif item == "G":
        Gs += 1
    elif item == "T":
        Ts += 1
    else:
        print(item, "is not a valid base")
        valid = False
if valid:
    print("Sequence length:", len(text))
    print("A:", As, "\nG:", Gs, "\nC:", Cs, "\nT:", Ts)

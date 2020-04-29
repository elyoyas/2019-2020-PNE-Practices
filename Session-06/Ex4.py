import termcolor
class Seq:
    def __init__(self, strbases):
        valid = True
        for base in strbases:
            if base == "A":
                pass
            elif base == "T":
                pass
            elif base == "C":
                pass
            elif base == "G":
                pass
            else:
                valid = False
                break
        if valid == True:
            self.strbases = strbases
            print("New sequence created!")
        elif valid == False:
            self.strbases = "ERROR"
            print("ERROR!!!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list,color):
    number = 0
    for item in seq_list:
        termcolor.cprint(f"Sequence{number}:(Length:{item.len()}) {item}",color)
        number += 1

def generate_seqs(pattern, number):
    seq_list = []
    content = pattern
    for n in range(0, number):
        seq_list.append(Seq(content))
        content = content + content
    return(seq_list)


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1,'blue')

print()
print("List 2:")
print_seqs(seq_list2,'green')

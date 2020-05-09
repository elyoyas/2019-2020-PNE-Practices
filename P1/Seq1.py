from pathlib import Path
class Seq:
    def __init__(self, strbases):
        valid = True
        full = False
        for base in strbases:
            if base in ["A", "C", "T", "G"]:
                full = True
                pass
            else:
                valid = False
                break
        if valid:
            if full:
                self.strbases = strbases
                print("New sequence created!")
            else:
                self.strbases = "NULL"
                print("NULL sequence created!")

        elif valid == False:
            self.strbases = "ERROR"
            print("ERROR!!!")
    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        if self.strbases in ["NULL","ERROR"]:
            return 0
        else:
            return len(self.strbases)
    def count_base(self, base):
        if self.strbases in ["NULL","ERROR"]:
            return 0
        else:
            count = 0
            for n in self.strbases:
                if n == base:
                    count += 1
            return count

    def seq_count(self):
        if self.strbases in ["NULL","ERROR"]:
            return {"A": 0, 'C': 0, 'T': 0, 'G': 0}
        else:
            count = {"A": 0, 'C': 0, 'T': 0, 'G': 0}
            for element in self.strbases:
                count[element] += 1
            return count

    def seq_reverse(self):
        if self.strbases in ["NULL","ERROR"]:
            return self.strbases
        else:
            reverse = ""
            letters = len(self.strbases) - 1
            while letters >= 0:
                reverse += (self.strbases[letters])
                letters -= 1
            return (reverse)

    def seq_complement(self):
        if self.strbases in ["NULL","ERROR"]:
            return self.strbases
        else:
            complemetary = ""
            for element in self.strbases:
                if element == "A":
                    complemetary += "T"
                elif element == "C":
                    complemetary += "G"
                elif element == "T":
                    complemetary += "A"
                else:
                    complemetary += "C"
            return (complemetary)
    def seq_read_fasta(self,filename):
        contents = Path(filename).read_text()
        lines = contents.split('\n')
        del (lines[0])
        self.strbases = str("".join(lines))
        return self
def print_seqs(seq_list, n):
    if type(seq_list) == Seq:
        print(f"Sequence {n} (Length:{seq_list.len()}) {seq_list}")
    elif type(seq_list) == list:
        number = 1
        for item in seq_list:
            print(f"Sequence{number}:(Length:{item.len()}) {item}")
            number += 1

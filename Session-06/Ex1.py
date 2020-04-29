class Seq:
    """A class for representing sequences"""

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
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
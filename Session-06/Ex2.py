class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        return len(self.strbases)

def print_seqs(seq_list):
    number = 0
    for item in seq_list:
        print(f"Sequence{number}:(Length:{item.len()}) {item}")
        number += 1
print_seqs([Seq("ACT"), Seq("GATA"), Seq("CAGATA")])
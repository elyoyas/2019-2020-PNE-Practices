from pathlib import Path


def seq_ping():
    print('OK')


def seq_read_fasta(filename):
    contents = Path(filename).read_text()
    lines = contents.split('\n')
    del (lines[0])
    string = "".join(lines)
    return string


def seq_len(seq):
    contents = Path(seq).read_text()
    lines = contents.split('\n')
    del (lines[0])
    DNA_string = ''.join(lines)
    return len(DNA_string)


def seq_count_base(seq, base):
    count = 0
    contents = Path(seq).read_text()
    lines = contents.split('\n')
    del (lines[0])
    DNA_string = ''.join(lines)
    for element in DNA_string:
        if element == base:
            count += 1
    return count


def seq_count(seq):
    contents = Path(seq).read_text()
    lines = contents.split('\n')
    del (lines[0])
    DNA_string = ''.join(lines)
    count = {"A": 0, 'C': 0, 'T': 0, 'G': 0}
    for element in DNA_string:
        count[element] += 1
    return count
def seq_reverse(seq):
    reverse = ""
    letters = len(seq) - 1
    while letters >= 0:
        reverse += (seq[letters])
        letters -= 1
    return(reverse)
def seq_complement(seq):
    complemetary = ""
    for element in seq:
        if element == "A":
            complemetary += "T"
        elif element == "C":
            complemetary += "G"
        elif element == "T":
            complemetary += "A"
        else:
            complemetary += "C"
    return(complemetary)
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


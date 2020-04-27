from seq0 import *
from pathlib import Path
FOLDER = "../Session-04/"
file = "U5.txt"
ahsoka = FOLDER+file

contents = Path(ahsoka).read_text()
lines = contents.split('\n')
del (lines[0])
anakin = ''.join(lines)

frag= anakin[:20]
print(" -----| Exercise 7 |------\nfragment:",frag,"\ncomplementary:",seq_complement(frag))

from pathlib import Path
file = "ADA.txt"
Content = Path(file).read_text()
lines = Content.split('\n')
del(lines[0])
length = 0
for item in lines:
    length += len(item)
print("Number of bases: ", length)

from pathlib import Path
file = "U5.txt"
Content = Path(file).read_text()
lines = Content.split('\n')
del(lines[0])
for item in lines:
    print(item, end= "\n")

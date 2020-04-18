from pathlib import Path

file = 'RNU6_269P.txt'
content = Path(file).read_text()
lines = content.split("\n")
print(line[0])

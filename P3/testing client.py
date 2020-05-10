from Client0 import Client
IP = "127.0.0.1"
PORT = 8090
c = Client(IP, PORT)
list_of_genes = ["U5", "ADA", "FRAT1", "FXN"]

print(f"Connection to SERVER at IP, PORT: {IP,PORT}")
print("Testing PING...")
print(c.talk("PING"))

print("*Testing GET...")
for number in range(-1,4):
    print(f"GET {number+1}: ", c.talk(str(f"GET {number}")))

print("\nTesting INFO...")
print(c.talk("INFO ATCCGTA"))

print("\nTesting COMP...")
print(c.talk("COMP AATCGACACTACGACGACATAGCTAGCACGA"))

print("\nTesting REV...")
print(c.talk("REV TGACGTACGACTACGTACGATCACACATGTACGTAGCAACATGACATCGATCACAGTACTAGGGACACTAGCTGAC"))

print("\nTesting GENE...")
for gene in list_of_genes:
    print(f"GENE: {gene}")
    print(c.talk(str(f"GENE {gene}")))


print("\nTesting CLOSE")
print(c.talk("CLOSE"))
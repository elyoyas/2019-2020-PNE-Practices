from seq0 import *
FOLDER = "../Session-04/"
files = ["U5", "ADA", "Frat1", "FXN","RNU6_269P"]

for file in files:
    print("GENE", file, "---> Length:", seq_len(FOLDER+file+".txt"))
import pickle
fin=open("fee.dat","rb")
try:
    while True:
        l=pickle.load(fin)
        print(l)
except EOFError:
    pass
fin.close()

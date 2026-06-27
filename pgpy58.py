import pickle 
def tf():
    f=open("fee.dat","rb")
    s=0
    try:
        while True:
            l=pickle.load(f)
            s+=l[3]
    except:
        f.close()
    return s
q=tf()
print(q)
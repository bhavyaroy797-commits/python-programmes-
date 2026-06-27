import pickle

def ttl_fees():
    ch = "y"
    f = open("fee.dat", "wb")
    total = 0  # 1. Start a counter at zero
    
    while ch in 'yY':
        rn = int(input("enter rno.:"))
        n = input("enter name:")
        cl = int(input("enter class:"))
        fee = int(input("enter fee:"))
        total = total + fee  
        rec = [rn, n, cl, fee]
        pickle.dump(rec, f)
        ch = input("y/n:")
        
    f.close()
    return total
a = ttl_fees()
print("Total fees collected:", a)
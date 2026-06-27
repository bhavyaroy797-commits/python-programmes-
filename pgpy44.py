import pickle
ch='y'
f=open("student.dat","ab")
while ch in 'yY':
    roll=int(input("Enter roll no.: "))
    sn=input("Enter name: ")
    stu={"roll no.":roll,"name":sn}
    pickle.dump(stu,f)
    ch=input("Continue (y/n): ")
f.close()

import pickle
roll=int(input("enter roll no.:"))
sn=input("enter name:")
stu={"roll":roll,"name":sn}
f=open("stud.pkl.txt","wb")
pickle.dump(stu,f)
f.close()

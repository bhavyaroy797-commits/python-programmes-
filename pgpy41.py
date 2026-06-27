import pickle
f=open("stud.pkl.txt","wb")
l=["xyz","abc"]
pickle.dump(l,f)
f.close()

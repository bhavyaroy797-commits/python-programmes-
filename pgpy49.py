def Indexlist(L):
    lst=[]
    for i in range(len(L)):
        if L[i]%2==0:
            lst.append(i)
    return lst
L=[1,2,3,4,5,6,46]
print(Indexlist(L))

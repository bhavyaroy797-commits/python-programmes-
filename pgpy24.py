t=(9,18,27,36,45,54)
l=list(t)
l1=[]
for i in l:
    if i%6==0:
        l1.append(i)
t1=tuple(l1)
print(t1)

l1=list("examination")
l2=l1[1:-1]
new_list=[]
for i in l2:
    j=l2.index(i)
    if j%2==0:
        l1.remove(i)
print(l1)

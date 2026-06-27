f_l1=["a","b","c","p"]
f_l2=f_l1
f_l3=f_l1[:]
f_l2[0]="g"
f_l3[1]="k"
s=0
for ls in (f_l1,f_l2,f_l3):
    if ls[0]=="g":
        s+=1
    if ls[1]=="k":
        s+=20
print(s)


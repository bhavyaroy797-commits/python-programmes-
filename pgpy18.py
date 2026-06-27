def change(p,q=10):
    p=p*q
    q=q+p
    print(p,"#",q)
    return (q)
a=5
b=10
a=change(a)
b=change(a,b)
print(a,"#",b)
    
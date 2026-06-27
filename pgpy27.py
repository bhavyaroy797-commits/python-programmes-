a=-1
b=1
n=int(input("enter a no.:"))
i=1
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1
print(i)

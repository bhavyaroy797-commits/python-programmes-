l=[4,6,7,1,6,9,4]
def func(l):
    for i in range(len(l)):
        if (l[i]%3==0 and l[i]%2==0):
            l[i]+=1
    print(l)
    return(l)
print(l)
k=func(l)
print(k)

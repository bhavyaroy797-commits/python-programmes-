def indlist(s):
    l=[]
    for i in range(len(s)):
        if s[i] in 'aeiou':
            l.append(i)
    return l
s=input("enter string:  ")
print(indlist(s))


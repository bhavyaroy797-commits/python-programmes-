def encrypt(s):
    k=len(s)
    m=""
    for i in range(0,k):
        if(s[i].isupper()):
            m+=str(i)
        elif s[i].islower():
            m+=s[i].upper()
        else:
            m+="*"
    print(m)
encrypt('AdamasUniversity')
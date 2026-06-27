str="aabbcc"
c=3
while True:
    if str[0]=='a':
        str=str[2:]
    elif str[-1]=='b':
        str=str[:2]
    else:
        c+=1
        break
print(str)
print(c)


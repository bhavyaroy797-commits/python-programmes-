f=open('file.txt','r')
k=f.read()
c=0
for i in k:
    if i in 'aeiouAEIOU':
        c+=1
print(c)
f.close()

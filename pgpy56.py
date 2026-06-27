f=open('file.txt','r')
k=f.read().split()
for i in k:
    if i[0]=='s' or i[0]=='S':
        print(i)
f.close()

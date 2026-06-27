
fin=open("f:\\story.txt")
k=fin.read().split()
c=0
for i in k:
    if i.islower():
        c+=1
print(c)
fin.close()


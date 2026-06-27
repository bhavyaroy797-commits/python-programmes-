fin=open("f:\\story.txt")
k=fin.readlines()
c=0
for i in k:
    if i.startswith("The "):
        c+=1
print(c)
fin.close()

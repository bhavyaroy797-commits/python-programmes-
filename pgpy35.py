fin=open("f:\\story.txt")
k=fin.read()
c=0
for i in k:
    if "s" in k:
        c+=1
print(c)
fin.close()


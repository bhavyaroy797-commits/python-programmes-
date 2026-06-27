fin=open("f:\\story.txt")
k=fin.read().split()
for i in k:
    a=len(i)
    print(i,':',"no. of characters:",a)
fin.close()


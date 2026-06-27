f=open("stu2.txt",'w')
for i in range(5):
    n=input("enter name:  ")
    f.write(n+'\n')
f.close()


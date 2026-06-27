f = open("mark.txt", "w")
c = int(input('Enter the number of students: '))
for i in range(c):
    rn = input('Enter roll number of student: ')  
    n = input('Enter name of student: ')
    m = input('Enter marks of student: ')  
    r = rn + ' ' + n + ' ' + m + '\n'  
    f.write(r) 
f.close()


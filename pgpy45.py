
import csv
f = open("stu.csv", "r")
d = csv.reader(f)
next(d) 
for i in d:
    if int(i[2]) > 85:
        print(i)
f.close()
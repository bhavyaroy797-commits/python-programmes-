n = int(input("enter a no: "))
if n < 2:
    print("not a prime no.")
else:
    a= 0
    for i in range(2, n):
        if n % i == 0:
           a= a+ 1
           break
    if a == 0:
        print("prime no.")
    else:
        print("not a prime no.")
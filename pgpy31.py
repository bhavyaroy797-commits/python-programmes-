import math
def prime(n):
    if n < 2:
       print("not a prime no.")
    i = 2
    while i*i <= n:
        if n % i == 0:
           print("not a prime no.")
        i += 1
    print("prime no.")

n=int(input("enter a no."))
prime(n)
  

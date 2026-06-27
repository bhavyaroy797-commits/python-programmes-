def palind(s):
    if s==s[::-1]:
       print("it's a palindrome")
    else:
         print("not a palindrome")
s=input("enter string: ")
palind(s)

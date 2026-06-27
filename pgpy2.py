p=8
def sum(q,r=5):
    global p
    p=(r+q)**2
    print(p, end="#")
a=2
b=5
sum(b,a)
sum(r=3,q=2)

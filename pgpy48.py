def swaphalf(l):
    m=len(l) // 2
    return l[m:] + l[:m]
l = [100, 200, 300, 30, 40, 50]
output = swaphalf(l)
print(output)


def Alpha(n1, n2):
    if n1 > n2:
        print(n1 % n2)
    else:
        print(n2 / n1, "#", end=' ')

num = [10, 23, 14, 54, 32]
for C in range(4, 0, -1):
    A = num[C]
    B = num[C - 1]
    Alpha(A, B)


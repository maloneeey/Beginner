n = int(input())
p = list(map(int, input().split()))

swap = 0
flag = 0
while True:
    flag = 0
    for i in range(n-1):
        if p[i] == i+1:
            p[i], p[i+1] = p[i+1], p[i]
            flag = 1
            swap += 1
    if p[n-1] == n:
            p[n-1], p[n-2] = p[n-2], p[n-1]
            flag = 1
            swap += 1

    if flag == 0:
        print(swap)
        break
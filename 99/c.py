n = int(input())
res = n
for i in range(n+1):
    cnt = 0
    tmp = i
    while tmp > 0:
        t = 0
        while 6**t <= tmp:
            t += 1
        tmp -= 6**(t-1)
        cnt += 1
    tmp = n-i
    while tmp > 0:
        t = 0
        while 9**t <= tmp:
            t += 1
        tmp -= 9**(t-1)
        cnt += 1
    res = min(res, cnt)
print(res)
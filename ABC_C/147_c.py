n = int(input())
prf = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        prf[i].append((x-1, y))

res = 0
for i in range(1<<n):
    flg = True
    cnt = 0
    for j in range(n):
        if ( i >>j & 1 ) == 1:
            cnt += 1
    for j in range(n):
        if ( i >>j & 1 ) == 1:
            for x,y in prf[j]:
                if y == 0 and ( i >> x & 1 ) == 1:
                    flg = False
                if y == 1 and ( i >> x & 1 ) == 0:
                    flg = False
    if flg:
        res = max(res, cnt)
print(res)

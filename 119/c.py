n, a, b, c = map(int, input().split())
Bmb = [int(input()) for _ in range(n)]
ans = 10**9
for i in range(4**n):
    aa, bb, cc = 0, 0, 0
    cnt = 0
    for j in range(n):
        k = ( i >> (2*j) ) & 3
        if k == 1:
            if aa > 0:
                cnt += 10
            aa += Bmb[j]
        elif k == 2:
            if bb > 0:
                cnt += 10
            bb += Bmb[j]
        elif k == 3:
            if cc > 0:
                cnt += 10
            cc += Bmb[j]
    if aa == 0 or bb == 0 or cc == 0:
        continue
    cnt += abs(a-aa) + abs(b-bb) + abs(c-cc)
    ans = min(ans, cnt)
print(ans)
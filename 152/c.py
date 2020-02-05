n = int(input())
P = list(map(int, input().split()))
cnt, tmp = 0, P[0]
for p in P:
    if p <= tmp:
        cnt += 1
    tmp = min(tmp, p)
print(cnt)
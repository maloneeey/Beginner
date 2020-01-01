N, M = map(int, input().split())
cnt = [0]*M
for _ in range(N):
    ka = list(map(int, input().split()))
    for a in ka[1:]:
        cnt[a-1] += 1
res = 0
for num in cnt:
    if num == N:
        res += 1
print(res)
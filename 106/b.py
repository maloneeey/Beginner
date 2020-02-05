n = int(input())
ans = 0
for k in range(1, n+1, 2):
    cnt = 1
    for i in range(1, k):
        if k%i == 0:
            cnt += 1
    if cnt == 8:
        ans += 1
print(ans)
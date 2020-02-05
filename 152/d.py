n = int(input())
ans = 0
Cnt = [[0]*10 for _ in range(10)]
for i in range(1, n+1):
    x, y = int(str(i)[0]), int(str(i)[-1])
    Cnt[x][y] += 1
for i in range(1, 10):
    for j in range(1, 10):
        ans += Cnt[i][j]*Cnt[j][i]
print(ans)

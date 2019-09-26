n = int(input())
a = list(map(int, input().split()))
m = list(map(int, input().split()))
K = int(input())

dp = [[ -1 for _ in range(K+1)] for _ in range(n+1) ]

for i in range(n):
    for j in range(K):
        if dp[i][j] >= 0:
            dp[i+1][j] = m[i]
        elif j < a[i] or dp[i][j-a[i]] <= 0:
            pass
        else:
            dp[i+1][j] = dp[i+1][j-a[i]] - 1

if dp[n][K] >= 0:
    print("Yes")
else:
    print("No")
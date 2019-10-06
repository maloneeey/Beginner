n = int(input())
s = list(input())

dp = [ [0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        dp[i][j] = dp[i+1][j+1] + 1 if s[i]==s[j] else 0
import sys
input = sys.stdin.readline

DIV = 10**9+7
s = input()
n = len(s)-1
ary = [ (int(s[i]) if s[i] != '?' else -1) for i in range(n) ]
dp = [ [0 for _ in range(13)] for _ in range(n+1) ]
dp[0][0] = 1
for i in range(n):
    for j in range(10):
        if ary[i] != -1 and ary[i] != j:
            continue
        for k in range(13):
            dp[i+1][(k*10+j)%13] += dp[i][k]

    for j in range(13):
        dp[i+1][j] %= DIV
print(dp[n][5])

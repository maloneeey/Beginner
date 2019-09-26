n = int( input() )
m = int( input() )
M = int( input() )

dp = [[ 0 for _ in range(n+1)] for _ in range(m+1)]

dp[0][0] = 1
for i in range(1, m+1):
    for j in range(n+1):
        if j-i >= 0:
            dp[i][j] = ( dp[i-1][j] + dp[i][j-i]) % M
        else:
            dp[i][j] = dp[i-1][j]
print(dp[m][n])
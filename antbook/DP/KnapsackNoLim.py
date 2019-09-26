n = int( input() )
w, v = [], []
for _ in range(n):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)
W = int( input() )

dp = [[0 for i in range(W+1)] for j in range(n+1)]
for i in range(n):
    for j in range(W+1):
        if j < w[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max( dp[i][j], dp[i+1][j-w[i]]+v[i])

print(dp[n][W])
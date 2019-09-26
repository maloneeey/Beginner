n = int( input() )
w, v = [], []
for _ in range(n):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)
W = int( input() )

dp = [[0 for i in range(W+1)] for j in range(n+1)]
for i in range(n-1, -1, -1):
    for j in range(W+1):
        if j < w[i]:
            dp[i][j] = dp[i+1][j]
        else:
            dp[i][j] = max( dp[i+1][j], dp[i+1][j-w[i]]+v[i])

print(dp[0][W])
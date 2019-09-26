n = int(input())
w, v = [], []
for i in range(n):
    w_, v_ = map(int, input().split())
    w.append(w_)
    v.append(v_)
W = int(input())

v_sum = sum(v)
dp = [ [0 for _ in range(v_sum+1) ] for _ in range(n + 1) ]
for j in range(1, v_sum+1):
    dp[0][j] = 10000000
for i in range(n):
    for j in range(v_sum+1):
        if j < v[i]:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])

res = 0
for i in range(v_sum+1):
    if dp[n][i] <= W:
        res = i
print(res)
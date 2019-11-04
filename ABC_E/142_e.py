N, M = map(int, input().split())
a, b, c = [], [], []
for _ in range(M):
    a_, b_ = map(int, input().split())
    c_ = list( map(int, input().split()) )
    a.append(a_)
    b.append(b_)
    c.append(c_)

INF = 10**9
bit_dp = [INF for _ in range(2**N)]
bit_dp[0] = 0
for i in range(M):
    bit_n = 0
    for j in c[i]:
        bit_n |=  1 << j - 1
    for j in range(2**N):
        if bit_dp[j|bit_n] > bit_dp[j] + a[i]:
            bit_dp[j|bit_n] = bit_dp[j] + a[i]

res = -1 if bit_dp[-1] >= INF else bit_dp[-1]
print(res)




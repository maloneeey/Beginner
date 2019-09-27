p,q = map( int, input().split() )
A = list( map( int, input().split() ) )
INT_MAX = 100000

dp = [ [ 0 for _ in range(q+2)] for _ in range(q+1) ]
A.insert(0, 0)
A.insert(q+1, p+1)

for w in range(2, q+2):
    for i in range(q+2-w):
        j = i + w
        t = INT_MAX

        for k in range(i+1, j):
            t = min(t, dp[i][k] + dp[k][j])

        dp[i][j] = t+A[j]-A[i]-2

print(dp[0][q+1])
m, p, x = map(float, input().split())
m = int(m)
x = int(x)
dp = [ [ 0 for _ in range( (1<<m)+1 ) ] for _ in range(2) ]

n = 1 << m
prv, nxt = dp[0], dp[1]
prv[n] = 1.0

for _ in range(m):
    for i in range(n+1):
        jub = min(i, n-i)
        t = 0.0
        for j in range(jub+1):
            t = max(t, p*prv[i+j]+(1-p)*prv[i-j])
        nxt[i] = t
    prv, nxt = nxt, prv

i = int( x*n / (10**6) )
print( prv[i] )
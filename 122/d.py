MOD = 10**9+7
n = int(input())
dp = [[[ [0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
A, C, G, T = 0, 1, 2, 3
dp[0][3][3][3] = 1
for i in range(1, n+1):
    for s in range(4):
        for t in range(4):
            for u in range(4):
                for v in range(4):
                    if any( x==(t, u, v) for x in ((A,G,C), (A,C,G), (G,A,C)) ) or any( (A,G,C)==x for x in ((s,u,v), (s,t,v)) ):
                        continue
                    dp[i][t][u][v] = ( dp[i][t][u][v]+dp[i-1][s][t][u] )%MOD
print( sum( dp[n][i][j][k] for i in range(4) for j in range(4) for k in range(4) )%MOD )
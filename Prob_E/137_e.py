import sys
from scipy.sparse.csgraph import bellman_ford
input = sys.stdin.readline

n, m, p = map(int, input().split())
dist = [ [ 0 for _ in range(n) ] for _ in range(n) ]
for _ in range(m):
    a, b, c = map(int, input().split())
    c -= p
    if a!=b:
        dist[a-1][b-1] = -c

try:
    dist = bellman_ford( csgraph=dist )
    res = int(-dist[0][n-1])
    print( res if res>0 else 0 )
except:
    print(-1)
import sys
from bisect import bisect_right
input = sys.stdin.readline
INF = 10**18
a, b, q = map(int, input().split())
S = [-INF] + [ int(input()) for _ in range(a) ] + [INF]
T = [-INF] + [ int(input()) for _ in range(b) ] + [INF]

for i in range(q):
    x = int(input())
    c, d = bisect_right(S, x), bisect_right(T, x)
    ans = INF
    for s in S[c-1:c+1]:
        for t in T[d-1:d+1]:
            ans = min( ans, abs(t-x)+abs(s-t), abs(s-x)+abs(t-s) )
    print(ans)
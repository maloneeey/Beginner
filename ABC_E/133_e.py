import sys
from collections import deque
MOD = 10**9+7
input = sys.stdin.readline

N, K = map(int, input().split())
adj = [ [] for _ in range(N+1) ]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

ans = 1
que = deque( [(1, 0, K)] )

while que:
    u, p, k = que.popleft()
    ans = (ans*k) % MOD

    if p == 0:
        k_next = K-1
    else:
        k_next = K-2

    for v in adj[u]:
        if v == p:
            continue
        que.append( (v, u, k_next) )
        k_next -= 1

print(ans)
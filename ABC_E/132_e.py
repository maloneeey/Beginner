from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = 10**9
to = [ [] for _ in range(n) ]
dist = [ [INF]*n for _ in range(3) ]
for _ in range(m):
    u, v = map(int, input().split())
    to[u-1].append(v-1)
s, t = map(int, input().split())
s -= 1; t -= 1

dist[0][s] = 0
que = deque([(s, 0)])
while que:
    u, prv = que.popleft()
    d = dist[prv][u]
    cur = (prv+1) % 3
    if prv == 2:
        d += 1
    for v in to[u]:
        if dist[cur][v] != INF:
            continue
        que.append((v, cur))
        dist[cur][v] = d
print( dist[0][t] if dist[0][t] < INF else -1 )
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
edge = {}

for i in range(n-1):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
    edge[(a-1, b-1)] = i
    edge[(b-1, a-1)] = i

que = deque()
que.append(0)
usd = [0]+[-1]*(n-1)
ans = [0]*(n-1)

while que:
    v = que.pop()
    j = 1
    for u in adj[v]:
        if usd[u] < 0:
            if j == usd[v]:
                j += 1
            usd[u] = j
            ans[edge[(u, v)]] = j
            que.appendleft(u)
            j += 1
print(max(ans))
for a in ans:
    print(a)
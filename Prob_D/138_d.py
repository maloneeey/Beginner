from collections import deque
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
ab = [ tuple( map(int, input().split()) ) for _ in range(N-1) ]
px = [ tuple( map(int, input().split()) ) for _ in range(Q) ]

tree = [[] for _ in range(N)]
for a,b in ab:
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

score = [0 for _ in range(N)]
for p, x in px:
    p -= 1
    score[p] += x

res = [0 for _ in range(N)]
res[0] = score[0]
visit = [0 for _ in range(N)]
stack = [0]
while stack:
    v = stack.pop()
    visit[v] = 1
    for to in tree[v]:
        if visit[to]:
            continue
        stack.append(to)
        res[to] = res[v] + score[to]

print(*res)

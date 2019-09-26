from heapq import *
n, r = map(int, input().split())
es = []
for _ in range(r):
    x, y, cost = map(int, input().split())
    es.append([x, y, cost])
    es.append([y, x, cost])

dist1 = [ float("inf") for _ in range(n) ]
dist2 = [ float("inf") for _ in range(n) ]
q = []
heappush(q, (0, 0))

while not q:
    p = heappop(q)
    v = p[1]

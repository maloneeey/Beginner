import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
h = []
for i in range(n):
    heapq.heappush( h, -a[i])

for _ in range(m):
    cost = heapq.heappop(h)
    heapq.heappush( h, int(cost/2) )

print(-sum(h))
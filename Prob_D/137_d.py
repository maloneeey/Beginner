import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().split())
works = []
dct = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    dct[a].append(-b)

hq = []
res = 0
for i in range(1, m+1):
    for item in dct[i]:
        heappush(hq, item)
    if hq:
        res += heappop(hq)

print(-res)
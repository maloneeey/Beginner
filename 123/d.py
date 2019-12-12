from heapq import heappop, heappush
x, y, z, k = map(int, input().split())
cak = []
cak.append(sorted(list(map(int, input().split())), reverse=True))
cak.append(sorted(list(map(int, input().split())), reverse=True))
cak.append(sorted(list(map(int, input().split())), reverse=True))

def push(q, idx, i):
    if idx[i] + 1 < len(cak[i]):
        idx[i] += 1
    heappush( q, (-cak[0][idx[0]]-cak[1][idx[1]]-cak[2][idx[2]], ( idx[0], idx[1], idx[2] )))
    return

q = [(-cak[0][0]-cak[1][0]-cak[2][0], (0, 0, 0))]
for _ in range(k):
    res, idx = heappop(q)
    for i in range(3):
        push( q, idx, i)
    print(-res)

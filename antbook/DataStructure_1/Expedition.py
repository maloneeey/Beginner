import heapq
n, l, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.append(l)
b.append(0)

que = []
ans = 0
pos = 0
tank = p

for i in range(n):
    d = a[i] - pos

    while tank-d < 0:
        if not bool(que):
            ans = -10**7
        tank = tank + heapq.heappop(que)*(-1)
        ans = ans + 1

    tank = tank - d
    pos = a[i]
    heapq.heappush(que, -b[i])

if ans<0:
    print(-1)
else:
    print(ans)

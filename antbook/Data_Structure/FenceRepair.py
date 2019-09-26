import heapq
n = int(input())
l = list( map(int, input().split()) )

cost = 0
que = []

for i in range(n):
    heapq.heappush(que, l[i])

while len(que) > 1:
    l1 = heapq.heappop(que)
    l2 = heapq.heappop(que)

    cost = cost + l1 + l2
    heapq.heappush(que, l1+l2)

print(cost)
from heapq import *
n, m = map(int, input().split())
a = list( map(int, input().split()) )
card = []
for _ in range(m):
  b_, c_ = map(int, input().split())
  card.append([b_, c_])

heapify(a)
card.sort(key=lambda x:x[1], reverse=True)

for i in range(m):
  for _ in range(card[i][0]):
    if a[0]<card[i][1]:
      heappushpop(a, card[i][1])
    else:
      break
print(sum(a))
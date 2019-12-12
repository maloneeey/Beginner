from itertools import combinations
n, k = map(int, input().split())

m = (n-2)*(n-1)//2
if k > m:
    print(-1)
    exit()

E = []
for i in range(2, n+1):
    E.append((1, i))
E_add = list(combinations(range(2, n+1), 2))
for i in range(m-k):
    E.append(E_add[i])

print(len(E))
for e in E:
    print(*e)
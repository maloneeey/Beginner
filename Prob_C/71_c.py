n = int(input())
a = list(map(int, input().split()))

a = sorted(a, reverse=True)

count = 0
edge = []

i = 0
for _ in range(n-1):
    if a[i] == a[i+1]:
        count = count + 1
        edge.append(a[i])
        i = i + 1
        if count == 2:
            break
    i = i + 1

s = edge[0]*edge[1] if count == 2 else 0
print(s)
n = int(input())
matrix = [ list( map(int, input().split() )) for _ in range(n)]
a = [ -1 for _ in range(n) ]

res = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            a[i] = j

for i in range(n):
    pos = -1
    for j in range(i, n):
        if a[j] <= i:
            pos = j
            break

    for j in range(pos, i, -1):
        a[j], a[j-1] = a[j-1], a[j]
        res += 1

print(res)
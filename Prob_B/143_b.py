n = int(input())
d = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i):
        count += d[i]*d[j]
print(count)
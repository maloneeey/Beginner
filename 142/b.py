n, k = map(int, input().split())
h = list(map(int, input().split()))
num = 0
for i in range(n):
    if h[i] >= k:
        num += 1
print(num)

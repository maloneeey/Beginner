a, b, k = map(int, input().split())
kth = 0
for i in range( min(a, b), 0, -1 ):
    if a % i == 0 and b % i == 0:
        kth += 1
    if kth == k:
        ans = i
        break
print(ans)
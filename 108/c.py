n, k = map(int, input().split())
if k%2 != 0:
    cnt = n//k
else:
    cnt = n//k+(n-k//2)
print()
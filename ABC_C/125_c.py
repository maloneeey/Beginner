from fractions import gcd

n = int(input())
a = list(map(int, input().split()))
m = [0]*n

l, r = [0]*n, [0]*n
for i in range(1, n):
    l[i] = gcd(a[i-1], l[i-1])
    r[n-1-i] = gcd(r[n-i], a[n-i])

ans = 1
for a, b in zip(l, r):
    x = gcd(a, b)
    if ans < x:
        ans = x

print(ans)
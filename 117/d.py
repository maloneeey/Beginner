n, k = map(int, input().split())
A = list(map(int, input().split()))
m = len(bin(k))-2
One = [0]*m
for i in range(n):
    for j in range(m):
        if A[i] >> j & 1:
            One[j] += 1
x = 0
for j in range(m):
    one, zero = One[j], n-One[j]
    if zero > one:
        if k-2**j >= x:
            x += 2**j
ans = 0
for a in A:
    ans += a^x
print(ans)
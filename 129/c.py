import sys
input = sys.stdin.readline
MOD = 10**9+7

n, m = map(int, input().split())
a = [1]+[-1]*(n)
for _ in range(m):
    a[int(input())] = 0

a[1] *= -1
for i in range(2, n+1):
    if a[i] != 0:
        a[i] = ( max(0, a[i-1]) + max(0, a[i-2]) ) % MOD

print(a[-1])
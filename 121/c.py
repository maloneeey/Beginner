import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ary = []
for _ in range(n):
    ary.append(list(map(int, input().split())))
ary.sort()

res = 0
for (a, b) in ary:
    if m-b>0:
        m -= b
        res += a*b
    else:
        res += a*m
        break
print(res)
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
p = list(map(int, input().split()))
cnt = sum(p[0:k])
tmp = 0
for i in range(k, n):
    if p[i] + tmp - p[i-k] > 0:
        cnt += p[i]-p[i-k]+tmp
        tmp = 0
    else:
        tmp += p[i]-p[i-k]
print((cnt+k)/2)
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list( map(int, input().split()) )
f = list( map(int, input().split()) )
a.sort()
f.sort(reverse=True)
i = 0
pfm = [ a[i]*f[i] for i in range(n) ]
while k > 1:
    max()
print(pfm)
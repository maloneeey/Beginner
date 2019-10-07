n = int(input())
v = []
for _ in range(n-1):
    u_, v_, w_ = map(int, input().split())
    v.append( [u_, v_, w_] )

v.sort(key=0).sort(key=1)
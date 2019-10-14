from bisect import bisect_left, bisect_right
n = int(input())
a = list( map( int, input().split() ) )
b = list( map( int, input().split() ) )
c = list( map( int, input().split() ) )
d = list( map( int, input().split() ) )

cd = []

for i in range(n):
    for j in range(n):
        cd.append( c[i]+d[j] )
cd.sort()

res = 0
for i in range(n):
    for j in range(n):
        ab = -( a[i]+b[j] )
        res += bisect_right(cd, ab) - bisect_left(cd, ab)
print(res)

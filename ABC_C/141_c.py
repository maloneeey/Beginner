n, k, q = map(int, input().split())
a = []
sc = [ k for _ in range(n) ]

for _ in range(q):
    a_ = int(input())
    a.append(a_)

for i in range(q):
    sc[ a[i]-1 ] = sc[ a[i]-1 ] + 1

for i in range(n):
    print("Yes") if sc[i]>q else print("No")

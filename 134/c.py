n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())

b = sorted(a)
for x in a:
    print( b[-2] if x == b[-1] else b[-1] )
n, l = map(int, input().split())

apl = [ l+i for i in range(n) ]
tst = 100
for a in apl:
    if abs(a) < abs(tst):
        tst = a
print( sum(apl)-tst )
n = int(input())
k = int(input())
l = list( map(float, input().split()) )

def C(x):
    num = 0
    for i in range(n):
        num += int( l[i]/x )
    return num >= k

lb, ub = 0, max(l)
for _ in range(100):
    mid = ( lb+ub )/2
    if C(mid):
        lb = mid
    else:
        ub = mid
print("{:.2f}".format( int(ub*100)/100) )
n = int( input() )
m = int( input() )
x = list( map(int, input().split()) )

def C(d):
    last = 0
    for _ in range(1, m):
        crt = last + 1
        while crt<n and x[crt]-x[last]<d:
            crt += 1
        if crt == n:
            return False
        last = crt
        return True

x.sort()
lb, ub = 0, max(x)

while ub-lb > 1:
    mid = int( (lb+ub)/2 )
    if C(mid):
        lb = mid
    else:
        ub = mid

print(lb)
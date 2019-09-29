n = int( input() )
m = int( input() )
x = list( map(int, input().split()) )

def C(d):
    last = 0
    for i in range(1, m):
        crt = last + 1
        while crt<n and x[xrt]-x[last]<d:
            crt += 1
        if crt == n:
            return False
        last = crt
    return True


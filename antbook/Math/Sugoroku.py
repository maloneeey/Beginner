def extgcd(a, b, x, y):
    d = a
    if b != 0:
        d = extgcd(b, a%b, y, x)
        y = y - int(a/b) * x
    else:
        x=1
        y=0
    return d

a, b = map(int, input().split())
ext
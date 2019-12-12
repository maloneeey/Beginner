from fractions import gcd
a, b, c, d = map(int, input().split())

def lcm(x, y):
    return x*y//gcd(x,y)

def notDiv(a, c, d):
    return a - a//c - a//d + a//lcm(c, d)

print( notDiv(b, c, d)-notDiv(a-1, c, d) )
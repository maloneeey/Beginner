from math import tan, pi, cos, sqrt

a, b, x = map(int, input().split())
v = a*a*b
lft, rgt = 0, 180
for _ in range(100000):
    theta = (lft+rgt)/2
    height = a*tan(theta/180*pi)
    if height <= b:
        amnt = v - a*a*height/2
    else:
        c = (height - b)/tan(theta/180*pi)
        amnt = v - a*a*b/2 - a*b*c/2
    if x > amnt:
        rgt = theta
    else:
        lft = theta
print(theta)
w, h, x, y = map(int, input().split())

area  = w*h/2
mlt = 1 if x == w/2 and y == h/2 else 0
print(area, mlt)
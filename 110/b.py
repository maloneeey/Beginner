n, m, x, y = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

zx = max(x, max(X)); zy = min(y, min(Y))
print('No War') if zx < zy else print('War')
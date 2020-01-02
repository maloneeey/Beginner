n = int(input())
X, Y, H = [], [], []
for _ in range(n):
    x, y, h = map(int, input().split())
    X.append(x); Y.append(y); H.append(h)

for cx in range(101):
    for cy in range(101):
        for i in range(n):
            if H[i] > 0:
                ch = H[i] + abs(cx-X[i]) + abs(cy-Y[i])
                break
        flg = True
        for i in range(n):
            if H[i] != max(ch-abs(cx-X[i])-abs(cy-Y[i]), 0):
                flg = False
                break
        if flg:
            print(cx, cy, ch)
            exit()
from bisect import bisect_left

w, h, n = map(int, input().split())
x_1 = list( map(int, input().split()) )
x_2 = list( map(int, input().split()) )
y_1 = list( map(int, input().split()) )
y_2 = list( map(int, input().split()) )

def compress(x_1, x_2, w):
    xs = set([])
    for i in range(n):
        for d in range(-1, 2):
            tx_1, tx_2 = x_1[i]+d, x_2[i]+d
            if 1<=tx_1<=w: xs.add(tx_1)
            if 1<=tx_2<=w: xs.add(tx_2)
    xs = sorted(xs)
    del xs[-1]

    for i in range(n):
        x_1[i] = bisect_left(xs, x_1[i]) - xs[0]
        x_2[i] = bisect_left(xs, x_2[i]) - xs[0]

    return len(xs)

w = compress(x_1, x_2, w)
h = compress(y_1, y_2, h)

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

fld = [ [0 for _ in range(6*n)] for _ in range(6*n) ]
for i in range(n):
    for y in range( y_1[i], y_2[i]+1 ):
        for x in range( x_1[i], x_2[i]+1 ):
            fld[y][x] = 1

ans = 0
for y in range(h):
    for x in range(w):
        if fld[y][x]: continue
        ans += 1

        que = []
        que.append([x, y])
        while que:
            s = que.pop(0)

            for i in range(4):
                tx, ty = s[0] + dx[i], s[1] + dy[i]
                if tx<0 or w<=tx or ty<0 or h<=ty: continue
                if fld[ty][tx]==1: continue
                que.append([tx, ty])
                fld[ty][tx] = 1
print(ans)
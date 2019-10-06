from itertools import combinations_with_replacement
dx = (-1, 0, 0, 0, 1)
dy = (0, -1, 0, 1, 0)

m, n = map(int, input().split())
tile = []
for _ in range(m):
    clm = list( map(int, input().split()) )
    tile.append(clm)

def get(x, y):
    c = tile[x][y]
    for d in range(5):
        x_, y_ = x+dx[d], y+dy[d]
        if 0<=x_<m and 0<=y_<n:
            c += flip[x_][y_]
    return c%2

def calc():
    for i in range(1, m):
        for j in range(n):
            if get(i-1, j) != 0:
                flip[i][j] = 1

    for j in range(n):
        if get(m-1, j) != 0:
            return -1

    num = 0
    for i in range(m):
        num += sum(flip[i])
    return num

res = -1
nums = [0, 1]
for clm_0 in combinations_with_replacement(nums, 5):
    flip = [ [0 for _ in range(n)] for _ in range(m) ]
    num = calc()
    if num >= 0 and (res < 0 or res > num):
        res = num
        opt = flip

print("-------")
if res<0:
    print("IMPOSSIBLE")
else:
    for i in range(n):
        for j in range(n):
            print(opt[i][j], end=" ")
        print()
    print("-------")
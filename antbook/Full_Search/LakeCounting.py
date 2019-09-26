def dfs(x, y):
    field[x][y] = "."

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy
            if 0<=nx and nx<n and 0<=ny and ny<m and field[nx][ny]=='W':
                dfs(nx, ny)

n, m = map( int, input().split() )
field = [ list(input()) for i in range(n) ]

res = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 'W':
            dfs(i, j)
            res = res + 1

print(res)
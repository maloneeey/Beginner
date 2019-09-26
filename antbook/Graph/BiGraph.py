n, w = map( int, input().split() )
g = [ [] for _ in range(n) ]
color = [0] * n
for i in range(w):
    x, y = map( int, input().split() )
    g[x].append(y)
    g[y].append(x)

def dfs(v, c):
    color[v] = c
    for i in range( len( g[v] )):
        if color[ g[v][i] ] == c:
            return False
        elif color[ g[v][i] ] == 0 and not dfs( g[v][i], -c ):
            return False
    return True

flag = 1
for i in range(n):
    if color[i] == 0:
        if not dfs( i, 1 ):
            flag = 0

string = "Yes" if flag else "No"
print(string)
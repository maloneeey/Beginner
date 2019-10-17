n = int(input())
links = [ set() for _ in range(n) ]
ans = [ -1 for _ in range(n) ]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    links[u].add( (v,w) )
    links[v].add( (u,w) )

que = [ (0, 0, -1) ]
while que:
    v, d, p = que.pop()
    if d%2 == 0:
        ans[v] = 0
    else:
        ans[v] = 1
    for u,w in links[v]:
        if u==p:
            continue
        que.append( (u, d+w, v) )

print( '\n'.join(map(str, ans))  )
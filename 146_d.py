import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
cnt = 1
res = [
usd = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)

num = 0

stc = []
for a in adj[0]:
    stc.append( (0, a, [0]) )

while stc:
    u, v, clr = stc.popleft()
    usd[v].append(clr); usd[u].append(clr)

    for vv in adj[v]:
        if vv == u:
            continue
        else:
            stc.append(v, vv, )
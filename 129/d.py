import sys
input = sys.stdin.readline

H, W = map(int, input().split())
F = []
for _ in range(H):
    a = list(input())[:-1]
    F.append(a)

L = [[0]*(W+2) for _ in range(H+2)]
R = [[0]*(W+2) for _ in range(H+2)]
U = [[0]*(W+2) for _ in range(H+2)]
D = [[0]*(W+2) for _ in range(H+2)]

for h in range(1, H+1):
    f = F[h-1]
    l = L[h]
    for w in range(1, W+1):
        l[w] = l[w-1] + 1 if f[w-1] == '.' else 0
        U[h][w] = U[h-1][w] + 1 if f[w-1] == '.' else 0

for h in range(H, 0, -1):
    f = F[h-1]
    r = R[h]
    for w in range(W, 0, -1):
        r[w] = r[w+1] + 1 if f[w-1] == '.' else 0
        D[h][w] = D[h+1][w] + 1 if f[w-1] == '.' else 0

ans = 0
for h in range(1, H+1):
    l, r, u, d = L[h], R[h], U[h], D[h]
    ans = max( ans, max( l[w]+r[w]+u[w]+d[w] for w in range(1, W+1) ))
print(ans-3)
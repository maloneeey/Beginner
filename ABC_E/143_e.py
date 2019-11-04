import sys
from scipy.sparse.csgraph import floyd_warshall
input = sys.stdin.readline

INF = float('inf')
n, m, l = map(int, input().split())
table_1 = [ [0 for _ in range(n) ] for _ in range(n) ]
table_2 = [ [0 for _ in range(n) ] for _ in range(n) ]

for _ in range(m):
    a, b, c = map(int, input().split())
    if c<=l:
        table_1[a-1][b-1] = c
        table_1[b-1][a-1] = c

table_1 = floyd_warshall(csgraph=table_1, directed=False)

for i in range(n):
    for j in range(i+1, n):
        if table_1[i][j] <= l:
            table_2[i][j] = 1
            table_2[j][i] = 1

table_2 = floyd_warshall(csgraph=table_2, directed=False)

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    if table_2[s-1][t-1] == INF:
        print(-1)
    else:
        print(int(table_2[s-1][t-1])-1)
import heapq

E, V = map(int, input().split())
s = int(input())
v = []
d = []
es = []
for _ in range(V):
    x, y, cost = map(int, input().split())
    es.append([x, y, cost])
    es.append([y, x, cost])

class edge():
    def __init__(self, fr, to, cost):
        self.fr = fr
        self.to = to
        self.cost = cost

def bellFord(s):
    for i in range(len(v)):
        d.append(100000)
    print(d)
    d[s] = 0
    while True:
        update = False
        for i in range(len(es)):
            e = edge(es[i][0], es[i][1], es[i][2])
            if d[e.fr] != "INF" and d[e.to] > d[e.fr] + e.cost:
                d[e.to] = d[e.fr] + e.cost
                update = True
        if not update:
            break

bellFord(s)
print(d)
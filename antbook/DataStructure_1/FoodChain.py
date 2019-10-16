class UnionFind:
    def __init__(self, n):
        self.rank = [ 0 for _ in range(n) ]
        self.par = []
        for i in range(n):
            self.par.append(i)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find( self.par[x] )
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] = self.rank[x] + 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

n, k = map(int, input().split())
t_, x_, y_ = [], [], []
uf = UnionFind( n*3 )
ans = 0

for _ in range(k):
    t, x, y = map(int, input().split())
    x = x - 1
    y = y - 1

    if x<0 or n<=x or y<0 or n<=y:
        ans = ans + 1
        continue

    if t == 1:
        if uf.same(x, y+n) or uf.same(x, y+2*n) :
            ans = ans + 1
        else:
            uf.unite(x, y)
            uf.unite(x+n, y+n)
            uf.unite(x+2*n, y+2*n)
    else:
        if uf.same(x, y) or uf.same(x, y+2*n):
            ans = ans + 1
        else:
            uf.unite(x, y+n)
            uf.unite(x+n, y+2*n)
            uf.unite(x+2*n, y)
print(ans)

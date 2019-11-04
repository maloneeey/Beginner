class UnionFind:
    def __init__(self, n):
        self.table = [-1 for _ in range(n)]

    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1<=d2:
            self.table[r2] = r1
            if d1==d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    uf.union(x, y)

ans = 0
for v in uf.table:
    if v<0:
        ans += 1
print(ans)
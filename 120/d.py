n, m = map(int, input().split())
Ab = []
for _ in range(m):
    ab = list(map(int, input().split()))
    Ab.append( [ab[0]-1, ab[1]-1] )

class UnionFind:
    def __init__(self, n):
        self.table = [-1]*n

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
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1

ans = n*(n-1)//2
Ans = [ans]
uf = UnionFind(n)
for ab in Ab[-1:0:-1]:
    if not uf.find(ab[0], ab[1]):
        ans -= abs( uf.table[ uf._root(ab[0]) ]*uf.table[ uf._root(ab[1]) ])
        uf.union(ab[0], ab[1])
    Ans.append(ans)
for ans in Ans[-1::-1]:
    print(ans)
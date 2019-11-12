import sys

input = sys.stdin.readline


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
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2


class BIT:
    def __init__(self, n):
        self.bit = [0 for _ in range(n + 1)]
        self.size = n

    def bitSum(self, i):
        self.s = 0
        while i > 0:
            self.s += self.bit[i]
            i -= i & -i
        return self.s

    def bitAdd(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

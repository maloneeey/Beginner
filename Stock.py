import sys

input = sys.stdin.readline

def nck_tables(mod, n):
    fac = [1, 1] # 階乗テーブル
    ifac = [1, 1] #階乗の逆元テーブル
    inverse = [0, 1] #逆元テーブル

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac

def nck(n, k, mod, fac, ifac):
    """
    nCkを計算する
    """
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % mod

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

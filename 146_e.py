import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

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

bit = BIT(n)

for i in range(n):
    bit.bitAdd(i, a[i])

for 
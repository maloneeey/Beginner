n = int(input())
a = list( map(int, input().split()) )

class BIT:
    def __init__(self, n):
        self.bit = [ 0 for _ in range(n+1) ]
        self.size = n

    def sum(self, i):
        self.s = 0
        while i > 0:
            self.s += self.bit[i]
            i -=  i & -i
        return self.s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i +=  i & -i

b = BIT(n)
ans = 0
for i, j in enumerate(a):
    b.add(j, 1)
    ans += i - b.sum(j) + 1

print(ans)
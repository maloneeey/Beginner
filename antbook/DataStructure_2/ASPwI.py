class BIT:
    def __init__(self, n):
        self.bit = [ 0 for _ in range(n+1) ]
        self.size = n

    def bitSum(self, i):
        self.s = 0
        while i > 0:
            self.s += self.bit[i]
            i -=  i & -i
        return self.s

    def bitAdd(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i +=  i & -i

N, Q = map(int, input().split())
A = list( map(int, input().split()) )
B = BIT(N)
C = BIT(N)

for _ in range(N):

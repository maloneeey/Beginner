import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
d = list( map(int, input().split()) )
MOD = 998244353

c = Counter(d)

def count(c, iter):
    if c[0] != 1 or d[0] != 0:
        return 0

    res = 1
    for i in range(2, iter+2):
        for _ in range(c[i]):
            res *= c[i-1]%MOD
        res %= MOD
    return res%MOD

res = count(c, max(d))
print(res)
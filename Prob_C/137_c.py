import sys
from itertools import accumulate
input = sys.stdin.readline

def acm(x):
    ary = [ i for i in range(x) ]
    return sum(ary)

n = int(input())
strings = {}
for _ in range(n):
    obj = ('').join(sorted(input()))
    if obj in strings:
        strings[obj] += 1
    else:
        strings[obj] = 1

res = 0
for obj in strings:
    res += acm(strings[obj])
print(res)
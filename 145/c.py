from itertools import permutations
from math import sqrt, factorial

n = int(input())
x, y = [], []
for _ in range(n):
    x_, y_ = map(int, input().split())
    x.append(x_); y.append(y_)

routeSum = 0
perm = list(permutations(i for i in range(n)))
for route in perm:
    for i in range(n-1):
        routeSum += sqrt( (x[route[i]] - x[route[i+1]])**2 + (y[route[i]] - y[route[i+1]])**2 )

print(routeSum/factorial(n))
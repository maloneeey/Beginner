from math import floor, ceil
n = int(input())

cost = n / 1.08

if n == int(1.08*floor(cost)):
    print(floor(cost))
elif n == int(1.08*ceil(cost)):
    print(ceil(cost))
else:
    print(":(")
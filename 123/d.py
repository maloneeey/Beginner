from itertools import product
x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = sorted([a+b for a, b in product(A, B)], reverse=True)[:k]
E = sorted([c+d for c, d in product(C, D)], reverse=True)[:k]
[ print(ans) for ans in E ]
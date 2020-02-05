from itertools import permutations
n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
l = [i+1 for i in range(n)]
cnt = 0
for v in permutations(l, n):
    cnt += 1
    if v == P:
        p = cnt
    if v == Q:
        q = cnt
print(abs(p-q))
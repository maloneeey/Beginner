from bisect import bisect_left
n, k = map(int, input().split())
X = list(map(int, input().split()))

c = bisect_left( X, 0 )
Pos, Neg = X[c:], X[c-1::-1]
print(Pos, Neg)
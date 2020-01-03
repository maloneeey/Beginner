from fractions import gcd
n, x = map(int, input().split())
X = list(map(int, input().split()))

X = [ abs(y-x) for y in X ]
ans = X[0]
for y in X[1:]:
    ans = gcd(ans, y)
print(ans)
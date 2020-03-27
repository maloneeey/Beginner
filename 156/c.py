n = int(input())
X = list(map(int, input().split()))
ans = float('inf')
for x in range(1, 101):
    tmp = sum( [ (y-x)**2 for y in X ] )
    ans = min(tmp, ans)
print(ans)
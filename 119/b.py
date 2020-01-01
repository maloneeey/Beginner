n = int(input())
BTC = 38*10**4
ans = 0
for _ in range(n):
    x, u = input().split()
    x = int(x) if u == 'JPY' else float(x)*BTC
    ans += x
print(ans)
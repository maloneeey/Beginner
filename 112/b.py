n, t = map(int, input().split())
cost = 10**4
for _ in range(n):
    c, tt = map(int, input().split())
    if tt <= t:
        cost = min(cost, c)
print('TLE') if cost == 10**4 else print(cost)
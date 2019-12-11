n = int(input())
a = list(map(int, input().split()))
MOD = 10**9+7

res = 0
for dig in range(61):
    one = 0
    for i in a:
        if i & (1<<dig) != 0:
            one += 1
    res = (res + one*(n-one)*(1<<dig))%MOD
print(res)
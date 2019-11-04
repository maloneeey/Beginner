L, R = map(int, input().split())
MOD = 2019
res = 2019
R = min(R, L+MOD)
for i in range(L, R+1):
    for j in range(i+1, R+1):
        res = min(res, (i*j)%2019)
        if res == 0:
            break
print(res)
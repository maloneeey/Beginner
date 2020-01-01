MOD = 10**9+7
l = input()
dp0 = 0; dp1 = 1

for a in l:
    if a == '0':
        dp0 = dp0*3%MOD
    else:
        dp0 = (dp0*3+dp1) % MOD
        dp1 = dp1*2%MOD
print((dp0+dp1)%MOD)
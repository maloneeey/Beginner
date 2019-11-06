from scipy.special import comb
MOD = 10**9+7
n, k = map(int, input().split())

def comb_mod(a, b):
    return int(comb(a, b, exact=True)) % MOD

for i in range(1, k+1):
    blue = comb_mod(k-1, i-1)
    red = comb_mod(n-k+1, i)
    print((red*blue)%MOD)
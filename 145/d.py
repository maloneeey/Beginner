import sys
input = sys.stdin.readline

x, y = map(int, input().split())
MOD = 10**9+7

def nck_tables(mod, n):
    fac = [1, 1] # 階乗テーブル
    ifac = [1, 1] #階乗の逆元テーブル
    inverse = [0, 1] #逆元テーブル

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac

def nck(n, k, mod, fac, ifac):
    """
    nCkを計算する
    """
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % mod

if (x+y) % 3 != 0 or x > 2*y or y > 2*x:
    print(0)
    sys.exit()

times = (x+y)//3
k = max(x, y) - times
fac, ifac = nck_tables(MOD, times)
ans = nck(times, k, MOD, fac, ifac)
print(ans)
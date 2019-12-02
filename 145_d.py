import sys
x, y = map(int, input().split())
MOD = 10**9+7

def nck(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0

if (x+y) % 3 != 0:
    print(0)
    sys.exit()

times = (x+y)//3
one = (cnt - abs(x-y))//2 - abs(x-y)
print(cnt, one)

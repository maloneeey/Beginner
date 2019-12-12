a, b = map(int, input().split())
lar = max(a, b)
sma = min(a, b)

if lar-sma >= 2:
    print(lar*2-1)
else:
    print(lar+sma)
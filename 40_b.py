import sys
input = sys.stdin.readline

def dif(a, b):
    dif = 0
    if b[2] < a[2]:
        dif += a[2]-b[2]
    if b[1] > a[1]:
        dif += b[1]-a[1]
    return dif

n = int(input())
lar = [0, 0]
sml = [0, 0]
que = []
for _ in range(n):
    a = list(map(int, input().split()))
    a.insert(0, a[1]-a[0])
    que.append(a)

lar, sml = que[0], que[1]
for tmp in que[2:]:
    lar_dif = dif( lar, tmp )
    sml_dif = dif( sml, tmp )
    if lar_dif < sml_dif:
        lar = tmp
    else:
        sml = tmp

print(lar[2]+sml[2]-lar[1]-sml[1])
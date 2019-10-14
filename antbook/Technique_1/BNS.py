from bisect import bisect_left
n = int(input())
w = list( map(int, input().split()) )
v = list( map(int, input().split()) )
W = int(input())

ps = []

n_2 = int( n/2 )
for i in range( 1<<n_2 ):
    sw, sv = 0, 0
    for j in range(n_2):
        if i >> j & 1:
            sw += w[j]
            sv += v[j]
    ps.append( [sw, sv] )

ps.sort()
m = 1
for i in range(1, 1<<n_2):
    if ps[m-1][1] < ps[i][1]:
        m += 1
        ps[m] = ps[i]

res = 0
for i in range( 1<<(n-n_2) ):
    sw, sv = 0
    for j in range(n-n_2):
        if i>>j&1:
            sw += w[n_2+j]
            sv += v[n_2+j]

    if sw <= W:
        tv = (  

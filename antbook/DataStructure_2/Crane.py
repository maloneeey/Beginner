from math import sin,cos, pi
ST_SIZE = 1<<15 - 1

def init(k, l, r):
    ang[k], vx[k] = 0.0, 0.0

    if r-l == 1:
        vy[k] = L[l]
    else:
        lch, rch = k*2+1, k*2+2
        init( lch, l, (l+r)/2 )
        init( rch, (l+r)/2, r )
        vy[k] = vy[lch] + vy[rch]

def change(s, a, v, l, r):
    if s<=l: return
    elif s<r:
        lch, rch = v*2+1, v*2+2
        m = int( (l+r)/2 )
        change( s, a, lch, l, m )
        change( s, a, rch, m, r )
        if s<=m: ang[v] += a

        s, c = sin(ang[v]), cos(ang[v])
        vx[v] = vx[lch] + c*vx[rch] - s*vy[rch]
        vy[v] = vy[lch] + s*vx[rch] + c*vy[rch]

N, C = map(int, input().split())
L = list(map(int, input().split()))
S = list(map(int, input().split()))
A = list(map(int, input().split()))

ang = [ 0 for _ in range(ST_SIZE) ]
vx = [ 0 for _ in range(ST_SIZE) ]
vy = [ 0 for _ in range(ST_SIZE) ]
prv = [ pi for _ in range(1, N) ]
init(0, 0, N)

for i in range(C):
    s = S[i]
    a = A[i]/360*2*pi

    change(s, a-prv[s], 0, 0, N)
    prv[s] = a
    print("{:.2f} {:.2f}").format( vx[0], vy[0] )